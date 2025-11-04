# Minimal pandas example for tabular data
import pandas as pd

# Create a small DataFrame
data = {
    "order_id": [1, 2, 3, 4],
    "price": [15.0, 29.5, 42.0, 10.0],
    "category": ["A", "A", "B", "B"],
}
df = pd.DataFrame(data)

# Inspect
print("\n=== HEAD ===\n", df.head())

# Filter and aggregate
filtered = df[df["price"] > 20]
print("\n=== FILTERED (price > 20) ===\n", filtered)

summary = df.groupby("category")["price"].agg(["count", "mean", "sum"]).reset_index()
print("\n=== SUMMARY BY CATEGORY ===\n", summary)

# Save to CSV (artifacts)
out_path = "artifacts/summary_by_category.csv"
import os
os.makedirs("artifacts", exist_ok=True)
summary.to_csv(out_path, index=False)
print(f"\nSaved: {out_path}")
