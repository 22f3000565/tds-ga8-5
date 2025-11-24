# chart.py
# Generates a professional Seaborn barplot for customer satisfaction
# Author: 22f3000565@ds.study.iitm.ac.in

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -----------------------------
# Generate realistic synthetic data
# -----------------------------
np.random.seed(42)  # reproducibility

categories = [
    "Electronics", "Home Appliances", "Groceries",
    "Clothing", "Furniture", "Beauty & Wellness"
]

# Generate synthetic average satisfaction scores (1–5 scale)
scores = np.round(np.random.normal(loc=[4.1, 3.8, 4.3, 3.9, 4.0, 4.2], scale=0.15), 2)

df = pd.DataFrame({
    "Category": categories,
    "AvgSatisfaction": scores
})

# -----------------------------
# Seaborn professional styling
# -----------------------------
sns.set_style("whitegrid")
sns.set_context("talk")
palette = sns.color_palette("Blues_d")

# -----------------------------
# Create 512x512 figure → figsize(8,8) & dpi=64
# -----------------------------
plt.figure(figsize=(8, 8))

sns.barplot(
    data=df,
    x="Category",
    y="AvgSatisfaction",
    palette=palette
)

plt.title("Average Customer Satisfaction by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Average Satisfaction Score (1–5)")

plt.xticks(rotation=20)
plt.tight_layout()

# -----------------------------
# Export as 512×512 PNG
# -----------------------------
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
