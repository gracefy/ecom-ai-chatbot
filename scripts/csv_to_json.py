import csv
import json

csv_file = "data/product_cleaned.csv"

json_file = "data/products.json"

data = []

with open(csv_file, mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["price_inr"] = float(row["price_inr"])
        data.append(row)

with open(json_file, mode="w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Converted {csv_file} to {json_file} successfully.")
