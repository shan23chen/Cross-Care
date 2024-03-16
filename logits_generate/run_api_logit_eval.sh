#!/bin/bash

# Define an array of demographic choices
declare -a demographics=("race" "gender")

# Define an array of language choices
declare -a languages=("en" "zh" "es" "fr")

# Define an array for location_preprompt options
declare -a location_pre=("True" "False")

# Define an array for service_type options
declare -a service_type=("azure" "cohere")

# Loop for the API method without iterating model names
api_logit_method="api_eval_logit.py"

for service in "${service_type[@]}"; do
    for demographic in "${demographics[@]}"; do
        for language in "${languages[@]}"; do
            for loc_prep in "${location_pre[@]}"; do
                echo "Running ${api_logit_method} for Demographic: ${demographic}, location_preprompt: ${loc_prep}"
                conda run --name in_biased_learning python "logits_generate/${api_logit_method}" --demographic "${demographic}" --language "${language}" --location_preprompt "${loc_prep}" --service_type "${service}"
                echo "Completed: Method: ${api_logit_method}, Demographic: ${demographic}, location_preprompt: ${loc_prep}"
            done
        done
    done
done