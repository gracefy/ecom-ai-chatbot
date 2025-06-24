def build_prompt(user_query: str, retrieved_docs: list) -> str:
    """
    Build the full prompt for LLM based on user query and retrieved documents
    """
    system_instruction = (
        "You are a helpful shopping assistant. "
        "Use only the provided product information to answer user questions. "
        "Generate a friendly markdown response listing relevant products."
    )

    context_block = ""
    for doc in retrieved_docs:
        context_block += f"[{doc['index']}] {doc['context']}\n"

    prompt = (
        f"{system_instruction}\n\n"
        f"User question: {user_query}\n\n"
        f"Here are some retrieved products:\n\n"
        f"{context_block}\n"
        f"Generate your response using the references like [1], [2] if applicable."
    )
    return prompt
