from openai import APIError
from typing import List, Optional
import time
import tiktoken
from backend.app.clients.openai_client import openai

EMBEDDING_MODEL = "text-embedding-ada-002"  # Default embedding model
EMBEDDING_MAX_TOKENS = 8192


def generate_embedding(text: str, model: str = EMBEDDING_MODEL) -> List[float]:
    """
    Generate embedding for a single text (realtime query usage)
    """

    _validate_text_input(text)

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

    for text in texts:
        _validate_text_input(text)

    max_retry = 3
    for attempt in range(max_retry):
        try:
            response = openai.embeddings.create(model=model, input=texts)
            embeddings = [item.embedding for item in response.data]
            return embeddings

        except APIError as e:
            print(f"[OpenAI API error] Attempt {attempt+1}: {e}")
            time.sleep(2**attempt)

        except Exception as e:
            print(f"[General unexpected error]: {e}")
            time.sleep(2**attempt)

    return [None] * len(texts)


def _validate_text_input(text: str, model: str = EMBEDDING_MODEL):
    if not text.strip():
        raise ValueError("Input text cannot be empty.")
    if _count_tokens(text, model) > EMBEDDING_MAX_TOKENS:
        raise ValueError(
            f"Input text exceeds model token limit ({EMBEDDING_MAX_TOKENS})"
        )


def _count_tokens(text: str, model: str = EMBEDDING_MODEL) -> int:
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))
