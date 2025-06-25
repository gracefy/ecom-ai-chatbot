from pydantic import BaseModel


class Product(BaseModel):
    product_id: str
    product_name: str
    product_brand: str
    description: str
    gender: str
    primary_color: str
    price_inr: float
