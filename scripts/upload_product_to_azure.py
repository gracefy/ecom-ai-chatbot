import pandas as pd
from backend.app.schemas.product_document import ProductDocument
from backend.app.clients.azure_client import search_client
from backend.app.services.openai_embedding_service import generate_embeddings_batch

BATCH_SIZE = 100
UPLOAD_BATCH_SIZE = 500


def upload_product_to_azure(input_path: str):
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

    # Build documents for Azure Search
    upload_documents = []
    for _, row in df.iterrows():
        doc = ProductDocument(
            product_id=str(row.product_id),
            product_name=str(row.product_name),
            brand=str(row.product_brand),
            gender=str(row.gender),
            color=str(row.primary_color),
            price=float(row.price_inr),
            description=str(row.description),
            context=str(row.context),
            embedding=list(row.embedding),
        )
        upload_documents.append(doc.model_dump())

    # Upload to Azure Search
    if upload_documents:
        total_batches = (
            len(upload_documents) + UPLOAD_BATCH_SIZE - 1
        ) // UPLOAD_BATCH_SIZE

        for i in range(0, len(upload_documents), UPLOAD_BATCH_SIZE):
            batch = upload_documents[i : i + UPLOAD_BATCH_SIZE]
            search_client.upload_documents(documents=batch)
            print(f"Uploaded batch {i // UPLOAD_BATCH_SIZE + 1} of {total_batches}")

        print("All documents uploaded successfully.")
    else:
        print("No documents to upload.")


if __name__ == "__main__":
    upload_product_to_azure("data/product_for_embedding.csv")
