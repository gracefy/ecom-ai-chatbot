import pandas as pd
from backend.app.services.embedding_service import generate_embeddings_batch

BATCH_SIZE = 100


def build_embedding_index(input_path: str, output_path: str):
    """
    Generate embeddings for full dataset in batches, build embedding index and save as pickle.
    """
    df = pd.read_csv(input_path)
    texts = df["context"].tolist()
    total_batches = (len(texts) + BATCH_SIZE - 1) // BATCH_SIZE

    all_embeddings = []

    # Process texts in batches
    for i in range(0, len(texts), BATCH_SIZE):
        batch_texts = texts[i : i + BATCH_SIZE]
        embeddings = generate_embeddings_batch(batch_texts)
        all_embeddings.extend(embeddings)

        print(f"Processed batch {i // BATCH_SIZE + 1}/{total_batches} ")

    # Add embeddings to DataFrame
    df["embedding"] = all_embeddings

    # Remove rows where embedding failed (i.e., None)
    df = df[df["embedding"].apply(lambda x: isinstance(x, list) and x is not None)]
    df = df.reset_index(drop=True)

    # Save the DataFrame with embeddings to a pickle file

    # Save final DataFrame with embeddings
    df.to_pickle(output_path)
    print(f"Embedding index saved to {output_path}")


if __name__ == "__main__":
    build_embedding_index(
        "data/product_for_embedding.csv", "data/product_embedding_index.pkl"
    )
