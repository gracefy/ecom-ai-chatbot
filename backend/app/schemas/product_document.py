from pydantic import BaseModel
from typing import Optional, List


class ProductDocument(BaseModel):
    product_id: str
    product_name: str
    brand: str
    gender: str
    color: str
    price: float
    description: str
    context: str
    embedding: List[float]
