import numpy as np
import pandas as pd
from backend.app.services.search_service import search_products


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
            "color_group": "Red",
            "price_inr": 2000.0,
            "embedding": generate_mock_embedding(),
        },
        {
            "product_id": "1002",
            "product_name": "Mock Product 2",
            "product_brand": "Mock Brand B",
            "gender": "Men",
            "color_group": "Blue",
            "price_inr": 3000.0,
            "embedding": generate_mock_embedding(),
        },
        {
            "product_id": "1003",
            "product_name": "Mock Product 3",
            "product_brand": "Mock Brand C",
            "gender": "Women",
            "color_group": "Red",
            "price_inr": 1500.0,
            "embedding": generate_mock_embedding(),
        },
        {
            "product_id": "1004",
            "product_name": "Mock Product 4",
            "product_brand": "Mock Brand D",
            "gender": "Boys",
            "color_group": "Yellow",
            "price_inr": 800.0,
            "embedding": generate_mock_embedding(),
        },
        {
            "product_id": "1005",
            "product_name": "Mock Product 5",
            "product_brand": "Mock Brand E",
            "gender": "Unisex",
            "color_group": "Pink",
            "price_inr": 5000.0,
            "embedding": generate_mock_embedding(),
        },
    ]
    return pd.DataFrame(data)


def run_test():
    embedding_df = build_mock_embedding_df()
    query_text = "Show me women's red dresses under 3000 INR"

    results = search_products(
        query_text, embedding_df=embedding_df, top_k=3, prefetch_k=5, bonus_weight=0.1
    )

    # Validate results
    assert isinstance(results, list)
    assert all(isinstance(r, dict) for r in results)
    assert len(results) == 3

    # Check required fields and data types in results
    for r in results:
        assert isinstance(r["product_id"], str)
        assert isinstance(r["product_name"], str)
        assert isinstance(r["product_brand"], str)
        assert isinstance(r["gender"], str)
        assert isinstance(r["color_group"], str)
        assert isinstance(r["price_inr"], float)

    # Check that results match the query criteria
    for r in results[:2]:
        assert r["gender"] == "Women"
        assert r["color_group"] == "Red"
        assert r["price_inr"] <= 3000

    # Check that results are sorted by final score
    final_scores = [r["final_score"] for r in results]
    assert final_scores == sorted(final_scores, reverse=True)

    # Print results for verification
    print("\n===== TEST SEARCH RESULTS =====")
    for row in results:
        print(row)


if __name__ == "__main__":
    run_test()
