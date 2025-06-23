import numpy as np
import pandas as pd
from backend.app.services.search_service import search_candidates


# Create mock embedding data for testing
def generate_mock_embedding():
    return np.random.rand(1536).tolist()


def build_mock_embedding_df():
    data = [
        {
            "product_id": "p1",
            "gender": "Women",
            "color_group": "Red",
            "price_inr": 2000,
            "embedding": generate_mock_embedding(),
        },
        {
            "product_id": "p2",
            "gender": "Men",
            "color_group": "Blue",
            "price_inr": 3000,
            "embedding": generate_mock_embedding(),
        },
        {
            "product_id": "p3",
            "gender": "Women",
            "color_group": "Red",
            "price_inr": 1500,
            "embedding": generate_mock_embedding(),
        },
        {
            "product_id": "p4",
            "gender": "Boys",
            "color_group": "Yellow",
            "price_inr": 800,
            "embedding": generate_mock_embedding(),
        },
        {
            "product_id": "p5",
            "gender": "Unisex",
            "color_group": "Pink",
            "price_inr": 5000,
            "embedding": generate_mock_embedding(),
        },
    ]
    return pd.DataFrame(data)


def run_test():
    embedding_df = build_mock_embedding_df()
    query_text = "Show me women's red dresses under 3000 INR"

    results = search_candidates(
        query_text, embedding_df, top_k=3, prefetch_k=5, bonus_weight=0.1
    )

    assert len(results) == 3
    assert (results.iloc[0:2]["gender"] == "Women").all()
    assert (results.iloc[0:2]["color_group"] == "Red").all()
    assert (results.iloc[0:2]["price_inr"] <= 3000).all()
    assert results.iloc[0]["filter_bonus"] >= results.iloc[2]["filter_bonus"]

    print("\n===== TEST SEARCH RESULTS =====")
    print(
        results[
            [
                "product_id",
                "gender",
                "color_group",
                "price_inr",
                "score",
                "filter_bonus",
                "final_score",
            ]
        ]
    )


if __name__ == "__main__":
    run_test()
