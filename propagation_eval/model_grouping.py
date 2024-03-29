all_models = ['EleutherAI/pythia-70m-deduped', 'state-spaces/mamba-130m',
       'EleutherAI/pythia-160m-deduped', 'EleutherAI/pile-t5-base',
       'state-spaces/mamba-370m', 'EleutherAI/pythia-410m-deduped',
       'EleutherAI/pile-t5-large', 'state-spaces/mamba-790m',
       'EleutherAI/pythia-1b-deduped', 'state-spaces/mamba-1.4b',
       'EleutherAI/pythia-2.8b-deduped', 'state-spaces/mamba-2.8b-slimpj',
       'state-spaces/mamba-2.8b', 'EleutherAI/pile-t5-xl',
       'EleutherAI/pythia-6.9b-deduped', 'Qwen/Qwen1.5-7B',
       'Qwen/Qwen1.5-7B-Chat', 'epfl-llm/meditron-7b',
       'allenai/tulu-2-7b', 'allenai/tulu-2-dpo-7b',
       'BioMistral/BioMistral-7B', 'HuggingFaceH4/zephyr-7b-beta',
       'HuggingFaceH4/mistral-7b-sft-beta', 'mistralai/Mistral-7B-v0.1',
       'mistralai/Mistral-7B-Instruct-v0.1', 'meta-llama/Llama-2-7b-hf',
       'meta-llama/Llama-2-7b-chat-hf', 'EleutherAI/pythia-12b-deduped',
       'meta-llama/Llama-2-70b-hf', 'meta-llama/Llama-2-70b-chat-hf',
       'epfl-llm/meditron-70b', 'allenai/tulu-2-70b',
       'allenai/tulu-2-dpo-70b', 'Qwen/Qwen1.5-72B',
       'Qwen/Qwen1.5-72B-Chat', 'gpt-35-turbo-0613', 'cohere'
]

pythia = ['EleutherAI/pythia-70m-deduped', 'EleutherAI/pythia-160m-deduped', 'EleutherAI/pythia-410m-deduped', 'EleutherAI/pythia-1b-deduped', 'EleutherAI/pythia-2.8b-deduped', 'EleutherAI/pythia-6.9b-deduped', 'EleutherAI/pythia-12b-deduped']
mamba = ['state-spaces/mamba-130m', 'state-spaces/mamba-370m', 'state-spaces/mamba-790m', 'state-spaces/mamba-1.4b', 'state-spaces/mamba-2.8b-slimpj', 'state-spaces/mamba-2.8b']
t5 = ['EleutherAI/pile-t5-base', 'EleutherAI/pile-t5-large', 'EleutherAI/pile-t5-xl']
qwen = ['Qwen/Qwen1.5-7B', 'Qwen/Qwen1.5-7B-Chat', 'Qwen/Qwen1.5-72B', 'Qwen/Qwen1.5-72B-Chat']
llama = ['allenai/tulu-2-7b', 'allenai/tulu-2-dpo-7b', 'allenai/tulu-2-70b', 'allenai/tulu-2-dpo-70b', 'meta-llama/Llama-2-7b-hf', 'meta-llama/Llama-2-7b-chat-hf', 'meta-llama/Llama-2-70b-hf', 'meta-llama/Llama-2-70b-chat-hf', 'epfl-llm/meditron-7b', 'epfl-llm/meditron-70b']
mistral = ['HuggingFaceH4/zephyr-7b-beta', 'HuggingFaceH4/mistral-7b-sft-beta', 'mistralai/Mistral-7B-v0.1', 'mistralai/Mistral-7B-Instruct-v0.1', 'BioMistral/BioMistral-7B']
api_model = ['gpt-35-turbo-0613', 'cohere']

model_group = {
    'pythia': pythia,
    'mamba': mamba,
    't5': t5,
    'qwen': qwen,
    'llama': llama,
    'mistral': mistral,
    'api_model': api_model
}

bio_comparison = ['meta-llama/Llama-2-7b-hf', 'epfl-llm/meditron-7b', 'mistralai/Mistral-7B-v0.1', 'BioMistral/BioMistral-7B']
model_size = ['Qwen/Qwen1.5-7B', 'Qwen/Qwen1.5-7B-Chat', 'Qwen/Qwen1.5-72B', 'Qwen/Qwen1.5-72B-Chat',  'meta-llama/Llama-2-7b-hf', 'meta-llama/Llama-2-7b-chat-hf', 'meta-llama/Llama-2-70b-hf', 'meta-llama/Llama-2-70b-chat-hf']
