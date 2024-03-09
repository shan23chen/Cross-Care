import os
import pandas as pd
import json
import sys
from templates import *
from openai_model import get_chat_completion
from tqdm import tqdm

# Determine the path to the root of the Cross-Care project dynamically
script_dir = os.path.dirname(
    os.path.realpath(__file__)
)  # Gets the directory where the script is located
cross_care_root = os.path.join(
    script_dir, "..", ".."
)  # Navigate up to the project root
cross_care_root = os.path.normpath(
    cross_care_root
)  # Normalize the path to ensure it's in the correct format

# Add the Cross-Care root to sys.path
sys.path.append(cross_care_root)

def find_missing(a, id_to_demo):
    """
    This function takes a list of data structures representing tokens and their log probabilities.
    It creates a new dictionary with either race or gender names as keys and their corresponding log probabilities as values.

    Args:
        a (list): A list of data structures representing tokens and their log probabilities.

    Returns:
        dict: A dictionary with either race or gender names as keys and their corresponding log probabilities as values.
    """
    temp_dict = {}
    for token_data in a:
        token_value = token_data.token
        if token_value.isdigit() and int(token_value) <= 5:
            temp_dict[token_value] = token_data.logprob
        else:
            print(token_value)

    if len(id_to_demo) > 4:
        # Assuming id_to_race is a dictionary mapping integer IDs to race names
        new_dict = {id_to_demo[int(key)]: value for key, value in temp_dict.items()}
    else:
        new_dict = {}
        # Assuming id_to_gender is a dictionary mapping integer IDs to gender names
        for key, value in temp_dict.items():
            if int(key) < 3:
                new_dict[id_to_demo[int(key)]] = value

    return new_dict


def eval_logits(
        diseases,
        prompt,
        templates,
        model_name,
        service="azure",
        id2demo = None,
):
    print(f'using {model_name} from {service}')
    
    def generate_statements(demographic, disease):
        return [
            template.format(demographic=demographic, disease=disease)
            for template in templates
        ]

    results = {disease: [] for disease in diseases}

    for disease in diseases:
        statements = generate_statements('__', disease)
        print(statements)
        all_log_softmax_sums = []
        for i in tqdm(range(0, len(statements), 1)):
            statement = statements[i]
            completion = get_chat_completion(statement+prompt, engine=model_name, service=service)
            log_softmax_values = find_missing(completion, id2demo)
            all_log_softmax_sums.append(log_softmax_values)

        results[disease].append(all_log_softmax_sums)

    return results


if __name__ == "__main__":
    import argparse
    import os

    parser = argparse.ArgumentParser(
        description="Run models on HF autoclass or mamba."
    )
    parser.add_argument(
        "--model_name",
        type=str,
        default="gpt-35-turbo-0613",
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
        "--service_type",
        type=str,
        default="azure",
        choices=["azure", "openai"],
        help="API end point to use for model inference, azure or openai",
    )
    parser.add_argument(
        "language",
        type=str,
        choices=["en", "es", "zh", "fr"],
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
        type=bool,
        default=False,
        help="Debug mode-> limit the number of diseases to 10. Default: False.",
    )

    args = parser.parse_args()

    model_name = args.model_name
    demographic_choice = args.demographic
    debug = args.debug

    print(f"Using model: {model_name}")
    print(f"Analyzing based on: {demographic_choice}")
    print(f"For language: {args.language}")

    # # Construct separate cache paths for models and tokenizers
    # model_cache_dir = os.path.join(cache_dir, "models", model_name)
    # tokenizer_cache_dir = os.path.join(cache_dir, "tokenizers", model_name)

    # # Ensure these directories exist
    # os.makedirs(model_cache_dir, exist_ok=True)
    # os.makedirs(tokenizer_cache_dir, exist_ok=True)

    ###### Load data ######
    pile_dir = (
        f"{cross_care_root}/output_pile/"  # Ensure cross_care_root is correctly defined
    )

    disease_demographic_templates = DiseaseDemographicTemplates()
    diseases = disease_demographic_templates.get_diseases(args.language)
    templates = disease_demographic_templates.get_templates(args.language)
    demographic_columns = disease_demographic_templates.get_demographics(args.language, demographic_choice)
    prompt = disease_demographic_templates.get_demographic_query(args.language, demographic_choice)
    id2demo = disease_demographic_templates.get_id2demo(args.language, demographic_choice)


    ###### Main logic ######
    print(diseases)
    print(templates)
    print(demographic_columns)
    print(prompt)
    # Evaluate logits and calculate averages for the chosen demographic
    out = eval_logits(
        diseases[:2],
        prompt=prompt,
        templates=templates,
        model_name=model_name,
        service=args.service_type,
        id2demo = id2demo
    )
    # a = calculate_average_log_softmax_per_demographic_disease(out)

    # Save the output
    output_dir = os.path.join(
        pile_dir, "openai", "logits", model_name.replace("/", "_")
    )  # Adjust for valid directory name
    os.makedirs(output_dir, exist_ok=True)

    output_file_path = os.path.join(output_dir, f"logits_{demographic_choice}_{args.language}.json")
    with open(output_file_path, "w") as f:
        json.dump(out, f)


# TODO 
# esay step to step whats going on: https://colab.research.google.com/drive/1zbQ9EYpsuao9jfIc-DaFE2Z9BaGwUuLG#scrollTo=8KAm7zOYK8FL&uniqifier=1
# for Jack, check if the code is working and if the output is as expected
# format it similar to our HF ones maybe?
# Openai templates can not have the 'empty base comparison' template, however i think is fine because it is formatted as MQA


