from fastapi import APIRouter, HTTPException, status
import pandas as pd
from typing import List
from backend.app.services.search_service import search_products
from backend.app.schemas.chat_schemas import ChatRequest, SearchResult

# Create a FastAPI router
router = APIRouter()


@router.post("/", response_model=List[SearchResult])
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
        results = search_products(query_text=query, top_k=request.top_k)

        # Convert records to SearchResult schema
        response = [SearchResult(**item) for item in results]

        return response

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
