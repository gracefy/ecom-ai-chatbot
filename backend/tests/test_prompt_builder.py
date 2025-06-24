import pytest
import random
from backend.app.services.prompt_builder import (
    build_prompt,
    CHAT_MODEL,
    CHAT_MAX_TOKENS,
    _count_tokens,
)
from backend.app.schemas.search_result import SearchResult


# ======= Prompt Builder Test =======
def test_prompt_builder(mock_retrieved_docs):
    user_query = "I want to buy running shoes under 3000 INR"
    prompt = build_prompt(user_query, mock_retrieved_docs)

    # Check if core parts exist in the final prompt
    assert "You are a helpful shopping assistant" in prompt
    assert "User question: I want to buy running shoes" in prompt
    assert "Here are some retrieved products" in prompt

    # Verify document reference markers exist
    assert "[1]" in prompt
    assert "[2]" in prompt

    total_tokens = _count_tokens(prompt, model=CHAT_MODEL)
    assert total_tokens <= CHAT_MAX_TOKENS


# ========== Edge Cases ==========
# ---------- Empty retrieved_docs ----------
def test_prompt_builder_empty_docs():
    user_query = "What products do you have?"
    retrieved_docs = []
    prompt = build_prompt(user_query, retrieved_docs)
    assert "Here are some retrieved products" in prompt
    total_tokens = _count_tokens(prompt, model=CHAT_MODEL)
    assert total_tokens <= CHAT_MAX_TOKENS


@pytest.fixture
def mock_retrieved_docs():
    return [
        SearchResult(
            index=1,
            context="Short context",
            product_id="p1",
            product_name="Product A",
            brand="Brand X",
            gender="Men",
            color="Red",
            price=1000.0,
            description="Desc",
            score=0.98,
        ),
        SearchResult(
            index=2,
            context="Another context",
            product_id="p2",
            product_name="Product B",
            brand="Brand Y",
            gender="Women",
            color="Blue",
            price=2000.0,
            description="Desc",
            score=0.95,
        ),
    ]
