from pydantic import BaseModel


class SearchResult(BaseModel):
    index: int
    product_id: str
    product_name: str
    context: str
    score: float
