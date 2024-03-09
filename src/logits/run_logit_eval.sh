#!/bin/bash

# Check if VRAM limit argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 VRAM_LIMIT_IN_GB"
    exit 1
fi

VRAM_LIMIT=$1

# Define an array of model names
declare -a model_names=(
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
)

# Define an associative array with model sizes in GB (approximations)
declare -A model_vram_requirements=(
    ["EleutherAI/pythia-70m-deduped"]=4  
    ["EleutherAI/pythia-160m-deduped"]=6
    ["EleutherAI/pythia-410m-deduped"]=8
    ["EleutherAI/pythia-1b-deduped"]=12
    ["EleutherAI/pythia-2.8b-deduped"]=24
    ["EleutherAI/pythia-6.9b-deduped"]=32
    ["EleutherAI/pythia-12b-deduped"]=48
    ["state-spaces/mamba-130m"]=6
    ["state-spaces/mamba-370m"]=8
    ["state-spaces/mamba-790m"]=16
    ["state-spaces/mamba-1.4b"]=24
    ["state-spaces/mamba-2.8b-slimpj"]=32
    ["state-spaces/mamba-2.8b"]=32
    ["EleutherAI/pile-t5-base"]=12
    ["EleutherAI/pile-t5-large"]=24
    ["EleutherAI/pile-t5-xl"]=32
    ["EleutherAI/pile-t5-xxl"]=48
)

# Define an array of demographic choices
declare -a demographics=("race" "gender")

# Loop through each model name
for model_name in "${model_names[@]}"
do
    model_size=${model_vram_requirements[$model_name]} # Corrected the array name here

    # Determine the device based on model size and VRAM limit
    if [ "$model_size" -le "$VRAM_LIMIT" ]; then
        device="cuda"
    else
        device="cpu"
    fi

    # Loop through each demographic
    for demographic in "${demographics[@]}"
    do
        echo "Running model inference for: $model_name, Demographic: $demographic, Device: $device"
        conda run --name in_biased_learning python Cross-Care/src/logits/logit_eval.py --model_name "$model_name" --demographic "$demographic" --device "$device"
        echo "Completed: $model_name, Demographic: $demographic"
    done
done
