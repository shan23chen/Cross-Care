from openai import AzureOpenAI
from openai import OpenAI

# GPT4V_KEY = ""
# openai_key = ''
SYS_PROMPT = 'You are an AI assistant, Please fill in the blank with only the numerical answer from the following choices'


def get_chat_completion(user_prompt, system_prompt=SYS_PROMPT,
                        engine='gpt-35-turbo-0613', service='',
                        temperature=0, max_tokens=1, top_p=0,
                        frequency_penalty=0, presence_penalty=0, stop=None):
    """
    Generates a chat completion using OpenAI's GPT model.

    Parameters:
    - user_prompt (str): The user's input prompt to the model.
    - system_prompt (str): The system's initial prompt setting the context for the model.
    - engine (str): The model you are using: [gpt-4, gpt4-32k, gpt-35-turbo-0613, 16k]
    - temperature (float): Controls randomness in the generation.
    - max_tokens (int): The maximum number of tokens to generate in the completion.
    - top_p (float): Nucleus sampling parameter controlling the size of the probability mass considered for token generation.
    - frequency_penalty (float): How much to penalize new tokens based on their frequency.
    - presence_penalty (float): How much to penalize new tokens based on their presence.
    - stop (list or None): Tokens at which to stop generating further tokens.

    Returns:
    - str: The generated completion text.
    """
    message_text = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    if service == 'azure':
        client = AzureOpenAI(
            azure_endpoint = "https://mgb-slt-openai-swissnorth.openai.azure.com/",
            api_key=GPT4V_KEY,
            api_version="2024-02-15-preview"
        )
        completion = client.chat.completions.create(
            model=engine,
            messages=message_text,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            stop=stop,
            logprobs=True,
            top_logprobs=5
        ).choices[0].logprobs.content[0].top_logprobs
        #['choices'][0]["logprobs"]['content'][0].top_logprobs
        return completion

    else:
        client = OpenAI(api_key=openai_key)
        response = client.chat.completions.create(
            model=engine,
            messages=message_text,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            stop=stop,
            logprobs=True,
            top_logprobs=5
        ).choices[0].logprobs.content[0].top_logprobs
        return response