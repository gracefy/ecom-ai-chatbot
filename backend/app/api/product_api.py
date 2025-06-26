import json
from fastapi import APIRouter, HTTPException, status
from backend.app.schemas.product import Product

router = APIRouter()

# Load product data at startup
with open("data/products.json", encoding="utf-8") as f:
    products = json.load(f)

product_lookup = {item["product_id"]: item for item in products}


@router.get("/product/{product_id}", response_model=Product)
def get_product(product_id: str):
    product = product_lookup.get(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
    return product
