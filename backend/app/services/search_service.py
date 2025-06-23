import numpy as np
import pandas as pd
from typing import Dict
from backend.app.services.embedding_service import generate_embedding
from backend.app.services.filter_extraction import extract_filters


# --- Search Logic ---
def search_candidates(
    query_text: str,
    embedding_df: pd.DataFrame,
    top_k: int = 5,
    prefetch_k: int = 100,
    bonus_weight: float = 0.1,
) -> pd.DataFrame:
    """
    Full search pipeline: vector search + soft filters + ranking.

    Args:
        query_text (str): User input query.
        embedding_df (pd.DataFrame): Pre-built embedding index.
        top_k (int): Final number of top results to return.
        prefetch_k (int): Prefetch candidates from vector search.
        bonus_weight (float): Weight for soft filter bonus.

    Returns:
        pd.DataFrame: Top-k search results.
    """

    # Extract filters from query
    filters = extract_filters(query_text)

    # Generate embedding for query
    query_embedding = generate_embedding(query_text)
    query_vector = np.array(query_embedding).reshape(1, -1)

    # Vector search
    embeddings_all = np.vstack(embedding_df["embedding"].tolist()).astype(np.float32)
    similarities = _cosine_similarity_batch(query_vector, embeddings_all)
    top_indices = np.argsort(similarities)[::-1][:prefetch_k]

    candidates = embedding_df.iloc[top_indices].copy()
    candidates["score"] = similarities[top_indices]

    # Soft filter bonus initialization
    candidates["filter_bonus"] = 0

    # Apply soft filters based on extracted attributes
    if "gender" in filters:
        candidates["filter_bonus"] += (
            candidates["gender"] == filters["gender"]
        ).astype(int)
    if "color_group" in filters:
        candidates["filter_bonus"] += (
            candidates["color_group"] == filters["color_group"]
        ).astype(int)
    if "min_price" in filters:
        candidates["filter_bonus"] += (
            candidates["price_inr"] >= filters["min_price"]
        ).astype(int)
    if "max_price" in filters:
        candidates["filter_bonus"] += (
            candidates["price_inr"] <= filters["max_price"]
        ).astype(int)

    # Calculate final score with bonus
    MAX_POSSIBLE_BONUS = 4
    candidates["normalized_bonus"] = candidates["filter_bonus"] / MAX_POSSIBLE_BONUS
    candidates["final_score"] = (
        candidates["score"] + bonus_weight * candidates["normalized_bonus"]
    )

    # Sort by final score and return top-k results
    final_results = candidates.sort_values("final_score", ascending=False).head(top_k)
    return final_results.reset_index(drop=True)


def _cosine_similarity_batch(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Compute cosine similarity between query vector and all embeddings.
    """
    a_norm = a / np.linalg.norm(a, axis=1, keepdims=True)
    b_norm = b / np.linalg.norm(b, axis=1, keepdims=True)
    return np.dot(a_norm, b_norm.T).flatten()
