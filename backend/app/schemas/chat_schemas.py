from pydantic import BaseModel
from typing import Optional


class ChatRequest(BaseModel):
    query: str
    top_k: Optional[int] = 5


class SearchResult(BaseModel):
    product_id: str
    product_name: str
    product_brand: str
    gender: str
    color_group: str
    price_inr: float
    final_score: float
