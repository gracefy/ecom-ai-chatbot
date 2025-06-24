from pydantic import BaseModel
from backend.app.schemas.search_result import SearchResult
from typing import List, Optional


class ChatRequest(BaseModel):
    query: str


class AnswerData(BaseModel):
    answer: str
    sources: List[SearchResult]


class ChatResponse(BaseModel):
    success: bool
    data: Optional[AnswerData] = None
    error: Optional[str] = None
