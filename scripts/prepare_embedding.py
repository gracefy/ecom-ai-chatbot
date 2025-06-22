import pandas as pd

FINAL_FIELDS = [
    "product_id",
    "product_name",
    "full_text",
    "product_brand",
    "gender",
    "price_inr",
    "primary_color",
    "color_group",
]

COLOR_MAPPING = {
    "Grey": "Grey",
    "Silver": "Grey",
    "Charcoal": "Grey",
    "Yellow": "Yellow",
    "Gold": "Yellow",
    "Mustard": "Yellow",
    "Orange": "Yellow",
    "Khaki": "Yellow",
    "Red": "Red",
    "Burgundy": "Red",
    "Maroon": "Red",
    "Blue": "Blue",
    "Navy": "Blue",
    "Pink": "Pink",
}

MAX_WORD_LENGTH = 400


def prepare_embedding(input_path: str, output_path: str):
    """
    Generate embeddings for cleaned data and export prepared dataset for indexing.
    """
    df = pd.read_csv(input_path)

    # Map color groups
    df["color_group"] = df["primary_color"].apply(_map_color_group)

    # Generate full text for embedding
    df["full_text"] = df.apply(
        lambda row: _generate_full_text(row["product_name"], row["description"]), axis=1
    )

    # Keep only relevant fields
    df = df[FINAL_FIELDS]

    df.to_csv(output_path, index=False)
    print(f"Prepared embedding data saved to {output_path}")


def _map_color_group(primary_color: str) -> str:
    return COLOR_MAPPING.get(primary_color, primary_color)


def _generate_full_text(name: str, description: str) -> str:
    name = str(name).strip().lower()
    description = str(description).strip().lower() if pd.notna(description) else ""
    full_text = f"{name}. {description}".strip()
    return _truncate_text(full_text)


def _truncate_text(text):
    words = text.split()
    return " ".join(words[:MAX_WORD_LENGTH])


if __name__ == "__main__":
    prepare_embedding("data/product_cleaned.csv", "data/product_for_embedding.csv")
