from pydantic import BaseModel


class SearchResult(BaseModel):
    index: int
    product_id: str
    product_name: str
    brand: str
    gender: str
    color: str
    price: float
    description: str
    context: str
    score: float
