#!/bin/bash

# Check if VRAM limit argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 VRAM_LIMIT_IN_GB"
    exit 1
fi

VRAM_LIMIT=$1

# Define an array of model names
declare -a hf_model_names=(
    # "Qwen/Qwen1.5-72B"
    # "Qwen/Qwen1.5-72B-Chat"
    "meta-llama/Llama-2-70b-hf"
    "meta-llama/Llama-2-70b-chat-hf"
    # "epfl-llm/meditron-70b"
    # "allenai/tulu-2-70b"
    # "allenai/tulu-2-dpo-70b"
)

# Define an associative array with model sizes in GB (approximations, less than 1GB will be annotated as 1)
declare -A model_vram_requirements=(
    # ["Qwen/Qwen1.5-72B"]=144
    # ["Qwen/Qwen1.5-72B-Chat"]=144
    ["meta-llama/Llama-2-70b-hf"]=140
    ["meta-llama/Llama-2-70b-chat-hf"]=140
    # ["epfl-llm/meditron-70b"]=140
    # ["allenai/tulu-2-70b"]=140
    # ["allenai/tulu-2-dpo-70b"]=140
)

# Define an array of demographic choices
declare -a demographics=("race" "gender")

# Define an array of language choices
declare -a languages=("en" "zh" "es" "fr")

# Define an array for location_preprompt options
declare -a location_pre=("True" "False")

# Loop for Hugging Face methods, iterating model names
declare -a hf_logit_methods=("hf_eval_logit.py" "hf_tf_eval_logit.py")
for model_name in "${hf_model_names[@]}"; do
    # Determine the device based on VRAM requirements
    model_vram=${model_vram_requirements[$model_name]}
    device="cuda"
    
    for demographic in "${demographics[@]}"; do
        for language in "${languages[@]}"; do
            for logit_method in "${hf_logit_methods[@]}"; do
                for loc_prep in "${location_pre[@]}"; do
                    echo "Running ${logit_method} for Model: ${model_name}, Demographic: ${demographic}, Language: ${language}, location_preprompt: ${loc_prep}, Device: ${device}"
                    # Pass the device as an argument to the Python script
                    conda run --name clinical_nlp python "logits_generate/${logit_method}" --model_name "${model_name}" --demographic "${demographic}" --language "${language}" --location_preprompt "${loc_prep}" --device "${device}" --cache_dir "/clinical_nlp/.cache"
                    echo "Completed: ${model_name}, Method: ${logit_method}, Demographic: ${demographic}, location_preprompt: ${loc_prep}, Device: ${device}"
                done
            done
        done
    done
done
