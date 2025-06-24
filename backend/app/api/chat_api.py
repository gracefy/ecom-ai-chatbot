from fastapi import APIRouter, HTTPException, status
from backend.app.services.vector_rag_service import generate_answer
from backend.app.schemas.chat_schemas import ChatRequest, ChatResponse

# Create a FastAPI router
router = APIRouter()


@router.post("/", response_model=ChatResponse, tags=["chat"])
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
        if len(query) > 500:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Query exceeds maximum length of 500 characters",
            )

        # Perform the search operation
        result = generate_answer(user_query=query)

        return ChatResponse(success=True, data=result, error=None)

    except Exception as e:
        return ChatResponse(success=False, data=None, error=str(e))
