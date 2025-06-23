import pandas as pd

FINAL_FIELDS = [
    "product_id",
    "product_name",
    "description",
    "product_brand",
    "gender",
    "price_inr",
    "primary_color",
    "context",
]


MAX_WORD_LENGTH = 400


def prepare_embedding(input_path: str, output_path: str):
    """
    Generate embeddings for cleaned data and export prepared dataset for indexing.
    """
    df = pd.read_csv(input_path)

    # Generate full text for embedding
    df["context"] = df.apply(
        lambda row: _generate_context(
            row["product_name"],
            row["description"],
            row["product_brand"],
            row["primary_color"],
            row["gender"],
            row["price_inr"],
        ),
        axis=1,
    )

    # Keep only relevant fields
    df = df[FINAL_FIELDS]

    df.to_csv(output_path, index=False)
    print(f"Prepared embedding data saved to {output_path}")


def _generate_context(product_name, description, brand, color, gender, price):
    return (
        f"Product Name: {product_name}. "
        f"Description: {description}. "
        f"Brand: {brand}. "
        f"Color: {color}. "
        f"Gender: {gender}. "
        f"Price: ₹{price}."
    )


def _truncate_text(text):
    words = text.split()
    return " ".join(words[:MAX_WORD_LENGTH])


if __name__ == "__main__":
    prepare_embedding("data/product_cleaned.csv", "data/product_for_embedding.csv")
