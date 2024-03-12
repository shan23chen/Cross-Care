import os
import pandas as pd
import json
import sys
from templates import *
from api_model import *
from tqdm import tqdm

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
        # else:
        #     print(token_value)

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
    demographics,
    diseases,
    system_prompt,
    prompt,
    templates,
    model_name,
    service="azure",
    id2demo=None,
):

    def generate_statements(demographic, disease):
        return [
            template.format(demographic=demographic, disease=disease)
            for template in templates
        ]

    # Initialize results dictionary with diseases as keys and empty dicts as values
    results = {disease: {} for disease in diseases}

    for disease in tqdm(diseases, desc="Processing Diseases"):
        for demographic in demographics:
            # Initialize an empty list for each demographic under each disease
            if demographic not in results[disease]:
                results[disease][demographic] = []

            statements = generate_statements(demographic, disease)

            all_log_softmax_sums = []

            if service == "cohere":
                for i in tqdm(range(0, len(statements), 1)):
                    statement = statements[i]
                    completion = get_chat_completion(
                        system_prompt,
                        statement + prompt,
                        engine=model_name,
                        service=service,
                    )
                    all_log_softmax_sums.append(completion)
            else:
                for i in tqdm(range(0, 2, 1)):
                    statement = statements[i]
                    completion = get_chat_completion(
                        system_prompt,
                        statement + prompt,
                        engine=model_name,
                        service=service,
                    )
                    log_softmax_values = find_missing(completion, id2demo)
                    all_log_softmax_sums.append(log_softmax_values)

            results[disease][demographic].append(all_log_softmax_sums)

    return results


def post_process_logits(input_file_path, total_templates):
    """
    Post-process the logits JSON to extract and format "true" logits, with imputation where necessary.

    Args:
    - input_file_path (str): Path to the input JSON file containing the raw logits data.
    - total_templates (int): The total number of templates used to generate the data.
    """
    # Load the existing data
    with open(input_file_path, "r") as file:
        data = json.load(file)

    # Process the data
    processed_data = {}
    for disease, demographics in data.items():
        processed_data[disease] = []
        for demographic, logits_list in demographics.items():
            true_logits = []
            for logits in logits_list:
                for logit_pair in logits:
                    # Extract "true" logit, impute 0 if "true" is not present
                    true_logit = logit_pair.get("true", 0)
                    true_logits.append(true_logit)

            # Ensure there are 'total_templates' entries, impute 0 if necessary
            true_logits += [0] * (total_templates - len(true_logits))
            processed_data[disease].append([demographic, true_logits])

    # Define the output path (you can also overwrite the original file if preferred)
    output_file_path = input_file_path.replace(".json", "_processed.json")

    # Save the processed data
    with open(output_file_path, "w") as file:
        json.dump(processed_data, file)

    return print(f"Processed logits saved to: {output_file_path}")


if __name__ == "__main__":
    import argparse
    import os

    parser = argparse.ArgumentParser(description="Run models on api end points")
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
        choices=["azure", "openai", "cohere"],
        help="API end point to use for model inference, azure or openai \n if you choose cohere, then it is going to use cohere api. Default: azure.",
    )
    parser.add_argument(
        "--language",
        type=str,
        choices=["en", "es", "zh", "fr"],
        default="en",  # Default
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
        help="Debug mode-> limit the number of diseases to 2. Default: False.",
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

    debug = args.debug

    print(f"Using model: {model_name}")
    print(f"Analyzing based on: {demographic_choice}")
    print(f"For language: {args.language}")

    ###### Load co-occurrence data ######
    co_occurrence_dir = f"{cross_care_root}/co_occurrence_results/output_pile/"  # Ensure cross_care_root is correctly defined

    disease_demographic_templates = DiseaseDemographicTemplates()
    diseases = disease_demographic_templates.get_diseases(language_choice)
    templates = disease_demographic_templates.get_templates(language_choice)
    demographic_columns = disease_demographic_templates.get_demographics(
        language_choice, demographic_choice
    )
    id2demo = disease_demographic_templates.get_id2tf()

    prompt = disease_demographic_templates.get_tf_query(language_choice)

    system_prompt = SYS_PROMPT

    if location_preprompt == True:
        location_prefix = disease_demographic_templates.get_tf_location_preprompt(
            language_choice
        )
        system_prompt = f"{system_prompt} {location_prefix}"

    if debug:
        diseases = diseases[:2]

    print(f"Analyzing the following diseases: {diseases}")

    ###### Main logic ######
    # Evaluate logits and calculate averages for the chosen demographic
    out = eval_logits(
        demographic_columns,
        diseases,
        system_prompt,
        prompt=prompt,
        templates=templates,
        model_name=model_name,
        service=args.service_type,
        id2demo=id2demo,
    )

    if location_preprompt == True:
        logits_dir = f"{cross_care_root}/logits_results/api/output_pile/{args.service_type}/american_context"  # Ensure cross_care_root is correctly defined
    else:
        logits_dir = f"{cross_care_root}/logits_results/api/output_pile/{args.service_type}/"  # Ensure cross_care_root is correctly defined

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

    # Process the logits data to save only the "true" logits
    if args.service_type == "cohere":
        print("no need to process logits for cohere")
    else:
        post_process_logits(output_file_path, len(templates))

# TODO - Add the following to the Cross-Care project:
# 1. Check all code
# 2. Check cohere works for other languages
# restructure this folder, clean methods, and add comments
        
