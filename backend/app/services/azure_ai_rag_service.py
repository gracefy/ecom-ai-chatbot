from backend.app.services.openai_chat_service import chat_completion
from backend.app.services.azure_ai_search_service import (
    azure_ai_search_products as search_products,
)
from backend.app.services.prompt_builder import build_prompt


def generate_answer_azure(user_query: str) -> dict:
    """Generate an answer based on the user query using vector search and chat completion.
    Args:
        user_query (str): The user's query to search for products.
    Returns:
        dict: A dictionary containing the answer and retrieved documents.
    Raises:
        ValueError: If the user query is empty.
    """

    if not user_query:
        raise ValueError("User query cannot be empty")

    system_instruction = (
        "You are a helpful shopping assistant. Answer user questions naturally."
        "Use only the provided product information to answer user questions. "
        "Generate a friendly markdown response listing relevant products."
        "Always cite sources like [1], [2] in the answer **for products you include in your response**."
    )

    retrieved_docs = search_products(user_query, top_k=5)
    prompt = build_prompt(user_query, retrieved_docs)

    messages = [
        {"role": "system", "content": system_instruction},
        {"role": "user", "content": prompt},
    ]
    answer = chat_completion(messages)

    return {
        "answer": answer,
        "sources": retrieved_docs,
    }
