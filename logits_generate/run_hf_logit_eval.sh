#!/bin/bash

# Check if VRAM limit argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 VRAM_LIMIT_IN_GB"
    exit 1
fi

VRAM_LIMIT=$1

# Define an array of model names
declare -a hf_model_names=(
    "EleutherAI/pythia-70m-deduped"
    "EleutherAI/pythia-160m-deduped"
    "EleutherAI/pythia-410m-deduped"
    "EleutherAI/pythia-1b-deduped"
    "EleutherAI/pythia-2.8b-deduped"
    "EleutherAI/pythia-6.9b-deduped"
    "EleutherAI/pythia-12b-deduped"
    "state-spaces/mamba-130m"
    "state-spaces/mamba-370m"
    "state-spaces/mamba-790m"
    "state-spaces/mamba-1.4b"
    "state-spaces/mamba-2.8b-slimpj"
    "state-spaces/mamba-2.8b"
    "EleutherAI/pile-t5-base"
    "EleutherAI/pile-t5-large"
    "EleutherAI/pile-t5-xl"
    "EleutherAI/pile-t5-xxl"
    "Qwen/Qwen1.5-7B"
    "Qwen/Qwen1.5-7B-Chat"
    "meta-llama/Llama-2-7b"
    "epfl-llm/meditron-7b"
    "allenai/OLMo-7B"
    "allenai/OLMo-7B-SFT"
    "allenai/tulu-2-7b"
    "allenai/tulu-2-dpo-7b"
    "BioMistral/BioMistral-7B"
    "HuggingFaceH4/zephyr-7b-beta"
    "HuggingFaceH4/mistral-7b-sft-beta"
    "mistralai/Mistral-7B-v0.1"
    "mistralai/Mistral-7B-Instruct-v0.1"
)

# Define an associative array with model sizes in GB (approximations, less than 1GB will be annotated as 1)
declare -A model_vram_requirements=(
    ["EleutherAI/pythia-70m-deduped"]=1
    ["EleutherAI/pythia-160m-deduped"]=1
    ["EleutherAI/pythia-410m-deduped"]=1
    ["EleutherAI/pythia-1b-deduped"]=2
    ["EleutherAI/pythia-2.8b-deduped"]=6
    ["EleutherAI/pythia-6.9b-deduped"]=14
    ["EleutherAI/pythia-12b-deduped"]=24
    ["state-spaces/mamba-130m"]=1
    ["state-spaces/mamba-370m"]=1
    ["state-spaces/mamba-790m"]=2
    ["state-spaces/mamba-1.4b"]=3
    ["state-spaces/mamba-2.8b-slimpj"]=6
    ["state-spaces/mamba-2.8b"]=6
    ["EleutherAI/pile-t5-base"]=1
    ["EleutherAI/pile-t5-large"]=3
    ["EleutherAI/pile-t5-xl"]=6
    ["EleutherAI/pile-t5-xxl"]=24
    ["Qwen/Qwen1.5-7B"]=14
    ["Qwen/Qwen1.5-7B-Chat"]=14
    ["meta-llama/Llama-2-7b"]=14
    ["epfl-llm/meditron-7b"]=14
    ["allenai/OLMo-7B"]=14
    ["allenai/OLMo-7B-SFT"]=14
    ["allenai/tulu-2-7b"]=14
    ["allenai/tulu-2-dpo-7b"]=14
    ["BioMistral/BioMistral-7B"]=14
    ["HuggingFaceH4/zephyr-7b-beta"]=14
    ["HuggingFaceH4/mistral-7b-sft-beta"]=14
    ["mistralai/Mistral-7B-v0.1"]=14
    ["mistralai/Mistral-7B-Instruct-v0.1"]=14
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
    if [ "$model_vram" -le "$VRAM_LIMIT" ]; then
        device="cuda"
    else
        device="cpu"
    fi

    for demographic in "${demographics[@]}"; do
        for language in "${languages[@]}"; do
            for logit_method in "${hf_logit_methods[@]}"; do
                for loc_prep in "${location_pre[@]}"; do
                    echo "Running ${logit_method} for Model: ${model_name}, Demographic: ${demographic}, Language: ${language}, location_preprompt: ${loc_prep}, Device: ${device}"
                    # Pass the device as an argument to the Python script
                    conda run --name in_biased_learning python "logits_generate/${logit_method}" --model_name "${model_name}" --demographic "${demographic}" --language "${language}" --location_preprompt "${loc_prep}" --device "${device}" --cache_dir "../../cache/"
                    echo "Completed: ${model_name}, Method: ${logit_method}, Demographic: ${demographic}, location_preprompt: ${loc_prep}, Device: ${device}"
                done
            done
        done
    done
done
