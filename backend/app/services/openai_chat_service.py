from openai import APIError
import time
from typing import List
from backend.app.clients.openai_client import openai

CHAT_MODEL = "gpt-3.5-turbo"  # Default chat model


def chat_completion(
    messages: List[dict], model: str = CHAT_MODEL, temperature: float = 0.3
) -> str:
    """
    Generate chat completion response from OpenAI API.

    Args:
        messages (List[dict]): List of message dictionaries containing role and content.
        model (str): The model to use for chat completion.

    Returns:
        str: The generated response from the model.
    """
    max_retry = 3

    for attempt in range(max_retry):
        try:
            response = openai.chat.completions.create(
                model=model, messages=messages, temperature=temperature, max_tokens=1024
            )
            return response.choices[0].message.content.strip()

        except APIError as e:
            print(f"[OpenAI API error] Attempt {attempt+1}: {e}")
            time.sleep(2**attempt)

        except Exception as e:
            print(f"[General unexpected error]: {e}")
            time.sleep(2**attempt)

    return ""
