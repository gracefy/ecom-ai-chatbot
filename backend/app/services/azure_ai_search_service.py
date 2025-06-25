from typing import List
from backend.app.clients.azure_client import search_client
from backend.app.schemas.search_result import SearchResult


def azure_ai_search_products(user_query: str, top_k: int = 5) -> List[dict]:

    results = search_client.search(search_text=user_query, top=top_k)

    retrieved_docs = []

    for idx, result in enumerate(results):
        doc = SearchResult(
            index=idx + 1,
            product_id=result["product_id"],
            product_name=result["product_name"],
            context=result["context"],
            score=result["@search.score"],
        )
        retrieved_docs.append(doc)

    return retrieved_docs
