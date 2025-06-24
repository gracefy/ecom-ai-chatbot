from pydantic import BaseModel
from backend.app.schemas.search_result import SearchResult
from typing import List


class ChatRequest(BaseModel):
    query: str


class ChatResponse(BaseModel):
    answer: str
    sources: List[SearchResult]
