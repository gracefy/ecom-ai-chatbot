import numpy as np
import pandas as pd
from backend.app.services.openai_client import generate_embedding

EMBEDDING_DF = pd.read_pickle("data/product_embedding_index.pkl")


# --- Search Logic ---
def search_products(
    query_text: str, embedding_df: pd.DataFrame = EMBEDDING_DF, top_k: int = 5
):
    # Generate embedding for query
    query_embedding = generate_embedding(query_text)

    # Vector search
    embeddings_vectors = np.vstack(embedding_df["embedding"].tolist()).astype(
        np.float32
    )
    query_vector = np.array(query_embedding).reshape(1, -1)

    similarity_scores = _cosine_similarity_batch(query_vector, embeddings_vectors)

    top_indices = similarity_scores.argsort()[::-1][:top_k]

    retrieved_docs = []
    for idx, row in enumerate(embedding_df.iloc[top_indices].itertuples(), 1):
        doc = {
            "index": idx,
            "context": row.context,
            "product_id": row.product_id,
            "product_name": row.product_name,
            "brand": row.product_brand,
            "gender": row.gender,
            "color": row.primary_color,
            "price": row.price_inr,
        }
        retrieved_docs.append(doc)

    return retrieved_docs


def _cosine_similarity_batch(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Compute cosine similarity between query vector and all embeddings.
    """
    a_norm = a / np.linalg.norm(a, axis=1, keepdims=True)
    b_norm = b / np.linalg.norm(b, axis=1, keepdims=True)
    return np.dot(a_norm, b_norm.T).flatten()
