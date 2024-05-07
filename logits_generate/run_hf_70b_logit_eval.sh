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
    # "meta-llama/Llama-2-70b-hf"
    # "meta-llama/Llama-2-70b-chat-hf"
    # "epfl-llm/meditron-70b"
    # "meta-llama/Llama-2-7b-hf"
    # "meta-llama/Llama-2-7b-chat-hf"
    # "epfl-llm/meditron-7b"
    "meta-llama/Meta-Llama-3-8B"
    "meta-llama/Meta-Llama-3-8B-Instruct"
    "meta-llama/Meta-Llama-3-70B"
    "meta-llama/Meta-Llama-3-70B-Instruct"
    # "allenai/tulu-2-70b"
    # "allenai/tulu-2-dpo-70b"
)

# Define an associative array with model sizes in GB (approximations, less than 1GB will be annotated as 1)
declare -A model_vram_requirements=(
    # ["Qwen/Qwen1.5-72B"]=144
    # ["Qwen/Qwen1.5-72B-Chat"]=144
    # ["meta-llama/Llama-2-70b-hf"]=140
    # ["meta-llama/Llama-2-70b-chat-hf"]=140
    # ["epfl-llm/meditron-70b"]=140
    # ["meta-llama/Llama-2-7b-hf"]=14
    # ["meta-llama/Llama-2-7b-chat-hf"]=14
    # ["epfl-llm/meditron-7b"]=14

    # ["allenai/tulu-2-70b"]=140
    # ["allenai/tulu-2-dpo-70b"]=140
    ["meta-llama/Meta-Llama-3-8B"]=16
    ["meta-llama/Meta-Llama-3-8B-Instruct"]=16
    ["meta-llama/Meta-Llama-3-70B"]=140
    ["meta-llama/Meta-Llama-3-70B-Instruct"]=140
)

# Define an array of demographic choices                                                
declare -a demographics=("race" "gender")
# declare -a demographics=("gender")

# Define an array of language choices
declare -a languages=("en" "zh" "es" "fr")
# declare -a languages=("es" "fr")

# Define an array for location_preprompt options
# declare -a location_pre=("True" "False")
declare -a location_pre=("True")

# Loop for Hugging Face methods, iterating model names
# declare -a hf_logit_methods=("70b_hf_eval_logit.py" "70b_hf_tf_eval_logit.py")
declare -a hf_logit_methods=("70b_hf_eval_logit.py")

# Define root directory for logits results
cross_care_root="/clinical_nlp/Cross-Care"


for model_name in "${hf_model_names[@]}"; do
    model_vram=${model_vram_requirements[$model_name]}
    if [ "$model_vram" -le "$VRAM_LIMIT" ]; then
        device="cuda"
    else
        device="cpu"
    fi

    for demographic in "${demographics[@]}"; do
        for language in "${languages[@]}"; do
            for logit_method in "${hf_logit_methods[@]}"; do
                # Extract "hf" or "hf_tf" from the logit_method for path construction
                logit_type=$(echo "$logit_method" | sed -e 's/_eval_logit.py//' -e 's/hf_tf_eval/hf_tf/' -e 's/hf_eval/hf/')

                for loc_prep in "${location_pre[@]}"; do
                    # Format model directory name by replacing slashes with underscores
                    model_dir_name=$(echo "$model_name" | sed 's/\//_/g')

                    if [ "$loc_prep" = "True" ]; then
                        # Define the full directory path including handling for american_context
                        logits_dir="${cross_care_root}/logits_results/${logit_type}/output_pile/american_context/${model_dir_name}/"
                    else
                        # Define the full directory path including handling for NON american_context
                        logits_dir="${cross_care_root}/logits_results/${logit_type}/output_pile/${model_dir_name}/"
                    fi

                    # Construct the expected logit file name and path
                    expected_filepath="${logits_dir}logits_${demographic}_${language}.json"

                    # Check if the logit file already exists
                    if [ -f "$expected_filepath" ]; then
                        echo "Skipping existing combination: File exists at ${expected_filepath}"
                    else
                        echo "no file at ${expected_filepath}"
                        echo "Running ${logit_method} for Model: ${model_name}, Demographic: ${demographic}, Language: ${language}, Location Prep: ${loc_prep}, Device: ${device}"
                        # Pass the device as an argument to the Python script
                        conda run --name clinical_nlp python "logits_generate/${logit_method}" --model_name "${model_name}" --demographic "${demographic}" --language "${language}" --location_preprompt "${loc_prep}" --device "${device}" --cache_dir "../cache"
                        echo "Completed: ${model_name}, Method: ${logit_method}, Demographic: ${demographic}, location_preprompt: ${loc_prep}, Device: ${device}"
                    fi
                done
            done
        done
    done
done
