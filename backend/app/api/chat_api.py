from fastapi import APIRouter, HTTPException, status
import pandas as pd
from typing import List
from backend.app.services.search_service import search_products
from backend.app.services.rag_service import generate_answer
from backend.app.schemas.chat_schemas import ChatRequest, SearchResult

# Create a FastAPI router
router = APIRouter()


@router.post("/")
async def chat(request: ChatRequest):
    """
    Handle chat queries and return search results.

    Args:
        query (str): User input query.

    Returns:
        dict: Search results.
    """
    try:
        # Call the search service with the user query
        query = request.query.strip()
        if not query:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Query cannot be empty"
            )

        # Perform the search operation
        results = generate_answer(user_query=query)

        # Convert records to SearchResult schema
        # response = [SearchResult(**item) for item in results]

        return results

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
