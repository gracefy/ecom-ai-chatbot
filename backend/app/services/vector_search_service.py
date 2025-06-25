import numpy as np
import pandas as pd
from typing import List
from backend.app.services.openai_embedding_service import generate_embedding
from backend.app.schemas.search_result import SearchResult

EMBEDDING_DF = pd.read_pickle("data/product_embedding_index.pkl")


# --- Search Logic ---
def search_products(
    user_query: str, embedding_df: pd.DataFrame = EMBEDDING_DF, top_k: int = 5
) -> List[dict]:
    # Generate embedding for query
    query_embedding = generate_embedding(user_query)

    # Vector search
    embeddings_vectors = np.vstack(embedding_df["embedding"].tolist()).astype(
        np.float32
    )
    query_vector = np.array(query_embedding).reshape(1, -1)

    similarity_scores = _cosine_similarity_batch(query_vector, embeddings_vectors)

    top_indices = similarity_scores.argsort()[::-1][:top_k]

    retrieved_docs = []

    # Iterate over the top indices to create a list of retrieved documents
    for idx, row_idx in enumerate(top_indices, 1):
        # Get the row from the original DataFrame using the index
        row = embedding_df.iloc[row_idx]

        # Create a document dictionary with relevant fields
        doc = SearchResult(
            index=idx,
            product_id=str(row.product_id),
            product_name=str(row.product_name),
            context=str(row.context),
            score=float(similarity_scores[row_idx]),
        )

        retrieved_docs.append(doc)

    return retrieved_docs


def _cosine_similarity_batch(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Compute cosine similarity between query vector and all embeddings.
    """
    a_norm = a / np.linalg.norm(a, axis=1, keepdims=True)
    b_norm = b / np.linalg.norm(b, axis=1, keepdims=True)
    return np.dot(a_norm, b_norm.T).flatten()
