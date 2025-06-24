import os
from dotenv import load_dotenv
from openai import OpenAI
from typing import List, Optional
import time

# Load API key from environment variable
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai = OpenAI(api_key=OPENAI_API_KEY)

EMBEDDING_MODEL = "text-embedding-ada-002"
CHAT_MODEL = "gpt-3.5-turbo"


def generate_embedding(text: str, model: str = EMBEDDING_MODEL) -> List[float]:
    """
    Generate embedding for a single text (realtime query usage)
    """
    response = openai.embeddings.create(model=model, input=text)
    return response.data[0].embedding


def generate_embeddings_batch(
    texts: List[str], model: str = EMBEDDING_MODEL
) -> List[Optional[List[float]]]:
    """
    Generate embeddings for a batch of texts (offline bulk processing)
    """
    if not texts:
        print("No input texts provided.")
        return []

    max_retry = 3
    for attempt in range(max_retry):
        try:
            response = openai.embeddings.create(model=model, input=texts)
            embeddings = [item.embedding for item in response.data]
            return embeddings

        except Exception as e:
            print(f"Batch embedding error: {e}, attempt {attempt+1}")
            time.sleep(2**attempt)

    return [None] * len(texts)


def chat_completion(messages: List[dict], model: str = CHAT_MODEL) -> str:
    """
    Generate chat completion response from OpenAI API.

    Args:
        messages (List[dict]): List of message dictionaries containing role and content.
        model (str): The model to use for chat completion.

    Returns:
        str: The generated response from the model.
    """
    try:
        response = openai.chat.completions.create(
            model=model, messages=messages, temperature=0.3, max_tokens=1024
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Chat completion error: {e}")
        return ""
