import torch
import inspect
import torch.nn.functional as F


def calculate_log_softmax_batch_seq2seq(texts, tokenizer, model, device):
    # Ensure eos_token_id is available and set it on model.config if necessary
    if not hasattr(model.config, "eos_token_id"):
        if hasattr(tokenizer, "eos_token_id"):
            model.config.eos_token_id = tokenizer.eos_token_id
            model.config.pad_token_id = tokenizer.eos_token_id
        else:
            print(
                "Warning: eos_token_id is not set on the model's configuration or tokenizer."
            )

    tokenizer.padding_side = "right"
    tokenizer.pad_token = tokenizer.eos_token
    model.config.pad_token_id = model.config.eos_token_id

    # Tokenize input texts
    inputs = tokenizer(
        texts,
        return_tensors="pt",
        padding="max_length",
        truncation=True,
        max_length=512,
    ).to(device)

    # Ensure eos_token_id and pad_token_id are set
    if not hasattr(model.config, "eos_token_id"):
        print("Warning: eos_token_id is not set on the model's configuration.")
    model.config.pad_token_id = tokenizer.pad_token_id

    # We should use a sequence of decoder_start_token_id repeated for each sequence in the batch, not just a single value.
    decoder_input_ids = torch.full_like(
        inputs["input_ids"], model.config.decoder_start_token_id
    )

    # Ensure we don't execute the model call inside an if block that's not required
    with torch.no_grad():
        outputs = model(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            decoder_input_ids=decoder_input_ids,  # Provide the prepared decoder_input_ids
        )

    logits = outputs.logits
    log_softmax_values = F.log_softmax(logits, dim=-1)

    log_softmax_sums = []
    for i in range(logits.shape[0]):  # Iterate over batch
        valid_indices = inputs["attention_mask"][
            i
        ].bool()  # Get valid indices based on attention mask
        # Sum log softmax values only over valid indices for each sequence
        seq_log_softmax_values = log_softmax_values[i][valid_indices]
        seq_log_softmax_sums = (
            seq_log_softmax_values.sum().item()
        )  # Summing over all valid positions
        log_softmax_sums.append(seq_log_softmax_sums)

    return log_softmax_sums


def calculate_log_softmax_batch_non_seq2seq(texts, tokenizer, model, device):
    # Ensure eos_token_id is available and set it on model.config if necessary
    if not hasattr(model.config, "eos_token_id"):
        if hasattr(tokenizer, "eos_token_id"):
            model.config.eos_token_id = tokenizer.eos_token_id
            model.config.pad_token_id = tokenizer.eos_token_id
        else:
            print(
                "Warning: eos_token_id is not set on the model's configuration or tokenizer."
            )

    tokenizer.padding_side = "right"
    tokenizer.pad_token = tokenizer.eos_token
    model.config.pad_token_id = model.config.eos_token_id

    # Adjust tokenization and model invocation based on model type
    inputs = tokenizer(
        texts, padding=True, return_tensors="pt", return_attention_mask=True
    )
    inputs = {k: v.to(device) for k, v in inputs.items()}

    # Check if 'attention_mask' is accepted by the model's forward method
    forward_signature = inspect.signature(model.forward)
    if "attention_mask" not in forward_signature.parameters:
        inputs.pop("attention_mask", None)

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    log_softmax_values = F.log_softmax(logits, dim=-1)

    input_ids = inputs["input_ids"]

    # Attention mask logic remains mostly relevant for non-T5 models
    attention_mask = inputs.get("attention_mask", None)
    if attention_mask is None:
        attention_mask = (input_ids != tokenizer.pad_token_id).long()

    # Logit extraction remains consistent across models
    gathered_log_softmax_values = log_softmax_values.gather(
        2, input_ids.unsqueeze(-1)
    ).squeeze(-1)
    masked_log_softmax_values = gathered_log_softmax_values * attention_mask
    log_softmax_sums = masked_log_softmax_values.sum(dim=1).tolist()

    return log_softmax_sums

