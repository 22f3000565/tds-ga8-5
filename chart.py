import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image

# Email included as comment for validation
# 22f3000565@ds.study.iitm.ac.in

# ----------------------------
# Generate synthetic dataset
# ----------------------------
categories = ["Electronics", "Clothing", "Home & Kitchen", "Sports", "Beauty"]
scores = [78, 82, 74, 88, 91]  # realistic customer satisfaction averages

df = pd.DataFrame({
    "Category": categories,
    "Satisfaction": scores
})

# ----------------------------
# Professional Seaborn styling
# ----------------------------
sns.set_style("whitegrid")
sns.set_context("talk")
palette = sns.color_palette("deep")

# ----------------------------
# Create the barplot
# ----------------------------
# Note: figsize does NOT guarantee exact pixels when saving.
plt.figure(figsize=(8, 8))  
sns.barplot(data=df, x="Category", y="Satisfaction", palette=palette)

plt.title("Average Customer Satisfaction by Product Category", fontsize=18)
plt.xlabel("Product Category")
plt.ylabel("Satisfaction Score")

# ----------------------------
# Save initial image
# ----------------------------
plt.savefig("chart_temp.png", dpi=64, bbox_inches="tight")
plt.close()

# ----------------------------
# Force image to EXACT 512×512 pixels
# ----------------------------
img = Image.open("chart_temp.png")
img = img.resize((512, 512), Image.LANCZOS)
img.save("chart.png")
