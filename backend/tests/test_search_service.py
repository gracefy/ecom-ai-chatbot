import numpy as np
import pandas as pd
from backend.app.services.vector_search_service import search_products
from backend.app.schemas.search_result import SearchResult


# Create mock embedding data for testing
def generate_mock_embedding():
    return np.random.rand(1536).tolist()


def build_mock_embedding_df():
    data = [
        {
            "product_id": "1001",
            "product_name": "Mock Product 1",
            "product_brand": "Mock Brand A",
            "gender": "Women",
            "primary_color": "Red",
            "price_inr": 2000.0,
            "description": "Red dress for women",
            "context": "Mock context 1",
            "embedding": generate_mock_embedding(),
        },
        {
            "product_id": "1002",
            "product_name": "Mock Product 2",
            "product_brand": "Mock Brand B",
            "gender": "Men",
            "primary_color": "Blue",
            "price_inr": 3000.0,
            "description": "Blue shoes for men",
            "context": "Mock context 2",
            "embedding": generate_mock_embedding(),
        },
        {
            "product_id": "1003",
            "product_name": "Mock Product 3",
            "product_brand": "Mock Brand C",
            "gender": "Women",
            "primary_color": "Red",
            "price_inr": 1500.0,
            "description": "Red party dress for women",
            "context": "Mock context 3",
            "embedding": generate_mock_embedding(),
        },
        {
            "product_id": "1004",
            "product_name": "Mock Product 4",
            "product_brand": "Mock Brand D",
            "gender": "Boys",
            "primary_color": "Yellow",
            "price_inr": 800.0,
            "description": "Yellow t-shirt for kids",
            "context": "Mock context 4",
            "embedding": generate_mock_embedding(),
        },
        {
            "product_id": "1005",
            "product_name": "Mock Product 5",
            "product_brand": "Mock Brand E",
            "gender": "Unisex",
            "primary_color": "Pink",
            "price_inr": 5000.0,
            "description": "Pink backpack for all",
            "context": "Mock context 5",
            "embedding": generate_mock_embedding(),
        },
    ]
    return pd.DataFrame(data)


def test_search_service():
    df = build_mock_embedding_df()
    query_text = "Show me women's red dresses under 3000 INR"

    results = search_products(query_text, embedding_df=df, top_k=3)

    # Validate results
    assert isinstance(results, list)
    assert all(isinstance(r, SearchResult) for r in results)
    assert len(results) == 3

    # Check that results are sorted by final score
    scores = [r.score for r in results]
    assert scores == sorted(scores, reverse=True)
