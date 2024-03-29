import os
import pandas as pd
import json
import sys
from tqdm import tqdm
import torch

from templates import *
from api_model import SYS_PROMPT
from hf_model import *

# Determine the path to the root of the Cross-Care project dynamically
script_dir = os.path.dirname(
    os.path.realpath(__file__)
)  # Gets the directory where the script is located
cross_care_root = os.path.join(script_dir, "..")  # Navigate up to the project root
cross_care_root = os.path.normpath(
    cross_care_root
)  # Normalize the path to ensure it's in the correct format

# Add the Cross-Care root to sys.path
sys.path.append(cross_care_root)

import torch
import torch.nn.functional as F


def eval_logits(
    demographics,
    diseases,
    system_prompt,
    prompt,
    model,
    tokenizer,
    model_type,
    device,
    batch_size=8,
    templates=None,
):
    def generate_statements(
        demographic, disease, system_prompt, user_prompt, templates
    ):
        """
        Generates full prompts for each statement.

        Args:
            demographic (str): The demographic group.
            disease (str): The disease being discussed.
            system_prompt (str): The system's instruction prompt.
            user_prompt (str): The user prompt that introduces the statement.
            templates (list): The list of statement templates.

        Returns:
            list: A list of fully constructed prompts.
        """
        full_prompts = []
        for template in templates:
            statement = template.format(demographic=demographic, disease=disease)
            full_prompt = f"{system_prompt} '{statement}' {user_prompt}"  # Constructs the full prompt
            full_prompts.append(full_prompt)

        return full_prompts

    def process_batch_non_seq2seq(texts, tokenizer, model, device):
        # Tokenize inputs and prepare for model inference
        inputs = tokenize_inputs(texts, model, tokenizer, device)
        # Perform model inference to get last token logits
        last_token_logits = model_inference(inputs, model)
        # Extract the log softmax value specifically for "1"
        log_softmax_for_true = extract_logit_for_true(last_token_logits, tokenizer)
        # Convert log softmax values for "True" to a list for easy handling
        log_softmax_for_true_list = log_softmax_for_true.cpu().numpy().tolist()

        return log_softmax_for_true_list

    def process_batch_seq2seq(texts, tokenizer, model, device):
        # Tokenize inputs and prepare for model inference
        inputs, targets = tokenize_for_seq2seq(texts, model, tokenizer, device)
        # Perform model inference
        logits = model_inference_seq2seq(inputs, targets, model)
        # Extract the log softmax value specifically for "1"
        log_softmax_for_true = extract_log_softmax_for_true_seq2seq(
            logits, targets, tokenizer
        )
        # Convert log softmax values for "True" to a list for handling
        log_softmax_for_true_list = log_softmax_for_true.cpu().numpy().tolist()

        return log_softmax_for_true_list

    results = {disease: [] for disease in diseases}

    for disease in tqdm(diseases, desc="Processing Diseases"):
        for demographic in demographics:
            # Generate full prompts for each combination of demographic and disease
            full_prompts = generate_statements(
                demographic, disease, system_prompt, prompt, templates
            )

            all_log_softmax_sums = []

            # Process in batches
            for i in range(0, len(full_prompts), batch_size):
                batch_prompts = full_prompts[i : i + batch_size]

                if model_type == "t5":
                    batch_log_softmax_sums = process_batch_seq2seq(
                        batch_prompts, tokenizer, model, device
                    )
                else:
                    batch_log_softmax_sums = process_batch_non_seq2seq(
                        batch_prompts, tokenizer, model, device
                    )

                all_log_softmax_sums.extend(batch_log_softmax_sums)

            # Store results
            results[disease].append((demographic, all_log_softmax_sums))

    return results


if __name__ == "__main__":
    import argparse
    import os

    from transformers import (
        AutoModelForCausalLM,
        AutoTokenizer,
        T5ForConditionalGeneration,
    )

    # from mamba_ssm.models.mixer_seq_simple import MambaLMHeadModel

    parser = argparse.ArgumentParser(description="Run models on HF autoclass or mamba.")
    parser.add_argument(
        "--model_name",
        type=str,
        default="EleutherAI/pythia-70m-deduped",
        help="Model name to use for inference",
    )
    parser.add_argument(
        "--demographic",
        type=str,
        choices=["race", "gender"],
        default="race",  # Default
        help="Demographic dimension to investigate: 'race' or 'gender'.",
    )
    parser.add_argument(
        "--batch_size",
        type=int,
        default=8,
        help="Batch size to use for parallel inference. Default: 8.",
    )
    parser.add_argument(
        "--device",
        type=str,
        default="cuda",
        choices=["cuda", "cpu"],
        help="Device to use for model inference: 'cuda' or 'cpu'. Default: 'cuda' if available.",
    )
    parser.add_argument(
        "--dtype",
        type=str,
        default="float16",
        choices=["float16", "float32"],
        help="Data type to use for model inference: 'float16' or 'float32'. Default: 'float16'.",
    )
    parser.add_argument(
        "--language",
        type=str,
        choices=["en", "es", "zh", "fr"],
        default="en",
        help="Language to use for the model. Options include 'en','es','zh' and 'fr'.",
    )
    parser.add_argument(
        "--cache_dir",
        type=str,
        default="cache",
        help="Cache directory to use for storing models and tokenizers. Default: '~/Desktop/mit/cache'.",
    )
    parser.add_argument(
        "--debug",
        type=lambda x: (str(x).lower() == "true"),
        help="Debug mode-> limit the number of diseases to 10. Default: False.",
    )
    parser.add_argument(
        "--location_preprompt",
        type=lambda x: (str(x).lower() == "true"),
        default=False,
        help="If True, the prompt will add the american location before the statement. Default: False.",
    )

    args = parser.parse_args()

    model_name = args.model_name
    demographic_choice = args.demographic
    language_choice = args.language
    location_preprompt = args.location_preprompt
    batch_size = args.batch_size
    device = args.device
    dtype = args.dtype
    cache_dir = args.cache_dir
    debug = args.debug

    print(f"Using model: {model_name}")
    print(f"Analyzing based on: {demographic_choice}")
    print(f"For language: {args.language}")

    # Construct separate cache paths for models and tokenizers
    model_cache_dir = os.path.join(cache_dir, "models", model_name)
    tokenizer_cache_dir = os.path.join(cache_dir, "tokenizers", model_name)

    # Ensure these directories exist
    os.makedirs(model_cache_dir, exist_ok=True)
    os.makedirs(tokenizer_cache_dir, exist_ok=True)

    # Determine model type
    is_mamba = model_name.startswith("state-spaces/mamba-")
    is_t5 = model_name.startswith("EleutherAI/pile-t5-")
    is_pythia = model_name.startswith("EleutherAI/pythia-")

    model_type = "mamba" if is_mamba else "t5" if is_t5 else "pythia"

    if is_mamba:
        # convert dtype to torch dtype
        dtype = torch.float16 if dtype == "float16" else torch.float32

        # Adjust if necessary. Assuming you're using a generic tokenizer for Mamba models as a placeholder
        tokenizer_model_name = "EleutherAI/gpt-neox-20b"  # This might be adjusted based on actual tokenizer used
        tokenizer = AutoTokenizer.from_pretrained(
            tokenizer_model_name, cache_dir=tokenizer_cache_dir
        )
        model = MambaLMHeadModel.from_pretrained(model_name, device=device, dtype=dtype)
        model.to(device).eval()
    elif is_t5:
        # tokenizer = UMT5Tokenizer.from_pretrained("EleutherAI/t5-v2-base")
        tokenizer = AutoTokenizer.from_pretrained(
            "oobabooga/llama-tokenizer", cache_dir=tokenizer_cache_dir
        )
        model = T5ForConditionalGeneration.from_pretrained(model_name)
        model.to(device).eval()
    else:
        # Load the specified model and tokenizer as before
        tokenizer = AutoTokenizer.from_pretrained(
            model_name, cache_dir=tokenizer_cache_dir
        )
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            cache_dir=model_cache_dir,
            # load_in_8bit=True
        )
        model.to(device).eval()
        model.eval()

    ###### Load co-occurrence data ######
    disease_demographic_templates = DiseaseDemographicTemplates()
    diseases = disease_demographic_templates.get_diseases(language_choice)
    templates = disease_demographic_templates.get_templates(language_choice)
    demographic_columns = disease_demographic_templates.get_demographics(
        language_choice, demographic_choice
    )
    prompt = disease_demographic_templates.get_tf_query(language_choice)

    system_prompt = SYS_PROMPT

    if location_preprompt:
        location_prefix = disease_demographic_templates.get_tf_location_preprompt(
            language_choice
        )
        system_prompt = f"{system_prompt} {location_prefix}"

    ###### Main logic ######

    # Evaluate logits and calculate averages for the chosen demographic
    out = eval_logits(
        demographic_columns,
        diseases,
        system_prompt,
        prompt,
        model,
        tokenizer,
        model_type,
        device,
        batch_size=batch_size,
        templates=templates,
    )

    if location_preprompt:
        logits_dir = f"{cross_care_root}/logits_results/hf_tf/output_pile/american_context/"  # Ensure cross_care_root is correctly defined
    else:
        logits_dir = f"{cross_care_root}/logits_results/hf_tf/output_pile/"  # Ensure cross_care_root is correctly defined

    # Save the output
    output_dir = os.path.join(
        logits_dir, model_name.replace("/", "_")
    )  # Adjust for valid directory name
    os.makedirs(output_dir, exist_ok=True)

    output_file_path = os.path.join(
        output_dir, f"logits_{demographic_choice}_{language_choice}.json"
    )
    with open(output_file_path, "w") as f:
        json.dump(out, f)

    # clear memory
    del model
    torch.cuda.empty_cache()
