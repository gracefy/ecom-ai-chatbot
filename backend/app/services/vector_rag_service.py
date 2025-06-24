from backend.app.services.openai_chat_service import chat_completion
from backend.app.services.vector_search_service import search_products
from backend.app.services.prompt_builder import build_prompt


def generate_answer(user_query: str) -> dict:
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

    retrieved_docs = search_products(user_query, top_k=5)
    prompt = build_prompt(user_query, retrieved_docs)

    messages = [
        {"role": "system", "content": "You are a helpful shopping assistant."},
        {"role": "user", "content": prompt},
    ]
    answer = chat_completion(messages)

    return {
        "answer": answer,
        "sources": retrieved_docs,
    }
