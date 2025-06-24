import numpy as np
import math
import pytest
from backend.app.services.openai_embedding_service import (
    generate_embedding,
    generate_embeddings_batch,
)


# ======== Test single embedding generation ========
def test_single_embedding():
    text = "Test product description"
    embedding = generate_embedding(text)

    # Basic assertions to check the type and length of the embedding
    assert isinstance(embedding, list)
    assert len(embedding) == 1536
    assert all(isinstance(v, (float, np.floating)) for v in embedding)

    # Check for None or NaN values
    assert all(v is not None for v in embedding)
    assert all(not math.isnan(v) for v in embedding)


# ======== Test batch embedding generation ========
def test_batch_embedding():
    texts = [
        "Test product description 1",
        "Test product description 2",
        "Test product description 3",
    ]
    embeddings = generate_embeddings_batch(texts)

    # Basic assertions to check the type and length of the embeddings
    assert isinstance(embeddings, list)
    assert len(embeddings) == 3

    # Check each embedding in the batch
    for embedding in embeddings:
        assert isinstance(embedding, list)
        assert len(embedding) == 1536
        assert all(isinstance(v, (float, np.floating)) for v in embedding)
        assert all(v is not None for v in embedding)
        assert all(not math.isnan(v) for v in embedding)


# ======== Edge Cases and Error Handling ========
def test_empty_input():
    with pytest.raises(ValueError):
        generate_embedding("")


def test_batch_empty_list():
    embeddings = generate_embeddings_batch([])
    assert embeddings == []


def test_batch_with_empty_string():
    texts = ["Test product 1", "", "Test product 3"]
    with pytest.raises(ValueError, match="Input text cannot be empty."):
        generate_embeddings_batch(texts)


def test_too_long_input():
    long_text = "very long text " * 10000
    with pytest.raises(ValueError):
        generate_embedding(long_text)


def test_batch_too_long_input():
    long_texts = ["very long text " * 10000, "short text"]

    with pytest.raises(ValueError):
        generate_embeddings_batch(long_texts)
