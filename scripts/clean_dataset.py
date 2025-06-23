import pandas as pd

RELEVANT_COLUMNS = [
    "ProductID",
    "ProductName",
    "Description",
    "ProductBrand",
    "Gender",
    "Price (INR)",
    "PrimaryColor",
]

COLUMN_MAPPING = {
    "ProductID": "product_id",
    "ProductName": "product_name",
    "ProductBrand": "product_brand",
    "Description": "description",
    "Gender": "gender",
    "Price (INR)": "price_inr",
    "PrimaryColor": "primary_color",
}

STRING_COLUMNS = [
    "product_id",
    "product_name",
    "product_brand",
    "description",
    "gender",
    "primary_color",
]


def clean_dataset(input_path: str, output_path: str):
    """
    Load raw data, clean and rename fields, remove duplicates, handle missing values,
    and export cleaned dataset.
    """
    df = pd.read_csv(input_path)

    # Keep only relevant columns
    df = df[RELEVANT_COLUMNS]

    # Rename columns
    df = df.rename(columns=COLUMN_MAPPING)

    # Handle missing values
    df = df.dropna()

    # remove spaces from string columns
    for col in STRING_COLUMNS:
        df[col] = df[col].astype(str).str.strip()

    # Correct data types
    dtype_mapping = {
        "product_id": "string",
        "product_name": "string",
        "product_brand": "string",
        "description": "string",
        "gender": "string",
        "primary_color": "string",
        "price_inr": "float64",
    }

    df = df.astype(dtype_mapping)

    df = df.drop_duplicates().reset_index(drop=True)

    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")


if __name__ == "__main__":
    clean_dataset("data/product_raw.csv", "data/product_cleaned.csv")
