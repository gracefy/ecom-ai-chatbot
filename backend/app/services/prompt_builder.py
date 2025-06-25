import tiktoken

CHAT_MODEL = "gpt-3.5-turbo"
CHAT_MAX_TOKENS = 16384  # Max tokens for chat completion


def build_prompt(user_query: str, retrieved_docs: list) -> str:
    """
    Build the full prompt for LLM based on user query and retrieved documents
    """
    if not user_query.strip():
        raise ValueError("User query cannot be empty.")

    context_block = ""

    total_tokens = _count_tokens(user_query, model=CHAT_MODEL)

    for doc in retrieved_docs:
        if not doc.context or not doc.context.strip():
            continue

        # Ensure the context is not too long for the chat model
        truncated_context = _truncate_text(doc.context)
        candidate_snippet = f"[{doc.index}] {truncated_context}\n"

        # Count tokens for the candidate snippet
        candidate_tokens = _count_tokens(candidate_snippet, model=CHAT_MODEL)

        if total_tokens + candidate_tokens > CHAT_MAX_TOKENS:
            break  # Stop if adding more context exceeds max tokens

        context_block += candidate_snippet
        total_tokens += candidate_tokens

    prompt = f"{user_query}\n\nContext:{context_block}\n"

    return prompt


# Truncate text to fit within the token limit for chat models
def _truncate_text(text: str, max_tokens: int = 200) -> str:
    encoding = tiktoken.encoding_for_model(CHAT_MODEL)
    tokens = encoding.encode(text)
    truncated_tokens = tokens[:max_tokens]

    return encoding.decode(truncated_tokens)


# Count tokens in a text for the specified model
def _count_tokens(text: str, model: str = CHAT_MODEL) -> int:
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))
