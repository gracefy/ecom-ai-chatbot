from backend.app.services.openai_client import chat_completion
from backend.app.services.search_service import search_products
from backend.app.services.prompt_service import build_prompt


def generate_answer(user_query: str) -> dict:

    retrieved_docs = search_products(user_query, top_k=5)
    prompt = build_prompt(user_query, retrieved_docs)

    messages = [
        {"role": "system", "content": "You are a helpful shopping assistant."},
        {"role": "user", "content": prompt},
    ]
    answer = chat_completion(messages)

    return {
        "answer": answer,
        "retrieved_docs": retrieved_docs,
    }
