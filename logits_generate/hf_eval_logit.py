import os
import pandas as pd
import json
import sys
from tqdm import tqdm

from templates import *
from hf_model import (
    calculate_log_softmax_batch_seq2seq,
    calculate_log_softmax_batch_non_seq2seq,
)
import torch

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


def eval_logits(
    demographics,
    diseases,
    model,
    tokenizer,
    model_type,
    device,
    batch_size=8,
    templates=None,
):
    def generate_statements(demographic, disease):
        return [
            template.format(demographic=demographic, disease=disease)
            for template in templates
        ]

    def process_combinations(demographic, disease):
        model.eval()
        statements = generate_statements(demographic, disease)
        all_log_softmax_sums = []

        for i in range(0, len(statements), batch_size):
            batch_statements = statements[i : i + batch_size]
            if model_type == "t5":
                batch_log_softmax_sums = calculate_log_softmax_batch_seq2seq(
                    batch_statements, tokenizer, model, device
                )
            else:
                batch_log_softmax_sums = calculate_log_softmax_batch_non_seq2seq(
                    batch_statements, tokenizer, model, device
                )

            all_log_softmax_sums.extend(batch_log_softmax_sums)

        return disease, demographic, all_log_softmax_sums

    results = {disease: [] for disease in diseases}

    for disease in tqdm(diseases, desc="Processing Diseases"):
        for demographic in demographics:
            _, _, log_softmax_values = process_combinations(demographic, disease)
            results[disease].append((demographic, log_softmax_values))

    return results


# def calculate_average_log_softmax_per_demographic_disease(output):
#     disease_averages = {}
#     for disease, demographic_results in output.items():
#         averages = {}
#         for demographic_result in demographic_results:
#             demographic, log_softmax_values = demographic_result
#             if demographic not in averages:
#                 averages[demographic] = []
#             averages[demographic].extend(log_softmax_values)

#         overall_averages = {
#             demographic: sum(values) / len(values) if values else float("inf")
#             for demographic, values in averages.items()
#         }

#         sorted_averages = sorted(overall_averages.items(), key=lambda x: x[1])
#         disease_averages[disease] = sorted_averages

#     # Nicely print the results
#     for disease, averages in disease_averages.items():
#         print(f"Disease: {disease}")
#         for rank, (race, avg) in enumerate(averages, start=1):
#             print(f"  {rank}. {race}: {avg:.2f}")
#         print()
#     return disease_averages


if __name__ == "__main__":
    import argparse
    import os

    from transformers import (
        AutoModelForCausalLM,
        AutoTokenizer,
        T5ForConditionalGeneration,
    )
    from mamba_ssm.models.mixer_seq_simple import MambaLMHeadModel

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
            model_name, cache_dir=model_cache_dir
        )
        model.to(device).eval()

    ###### Load co-occurrence data ######
    co_occurrence_dir = f"{cross_care_root}/co_occurrence_results/output_pile/"  # Ensure cross_care_root is correctly defined

    disease_demographic_templates = DiseaseDemographicTemplates()
    diseases = disease_demographic_templates.get_diseases(language_choice)
    templates = disease_demographic_templates.get_templates(language_choice)
    demographic_columns = disease_demographic_templates.get_demographics(
        language_choice, demographic_choice
    )

if location_preprompt:
    location_prefix = disease_demographic_templates.get_tf_location_preprompt(
        language_choice
    )
    # Prepend the location_prefix to each template in the list
    templates = [f"{location_prefix} {template}" for template in templates]
    print(f"Updated templates: {templates}")

    ###### Main logic ######

    # Evaluate logits and calculate averages for the chosen demographic
    out = eval_logits(
        demographic_columns,
        diseases,
        model,
        tokenizer,
        model_type,
        device,
        batch_size=batch_size,
        templates=templates,
    )

    if location_preprompt:
        logits_dir = f"{cross_care_root}/logits_results/hf/output_pile/american_context/"  # Ensure cross_care_root is correctly defined
    else:
        logits_dir = f"{cross_care_root}/logits_results/hf/output_pile/"  # Ensure cross_care_root is correctly defined

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


# TODO
# for Jack, check if the code is working and if the output is as expected
# bash for all the model we are interested in
