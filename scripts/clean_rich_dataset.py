import pandas as pd

# Load rich dataset
df = pd.read_csv("data/rich/emotion_rich.csv")

# Drop rows with emotion == "surprise"
df_cleaned = df[df["label"] != 5]

# Save cleaned version
df_cleaned.to_csv("data/rich/emotion_rich_cleaned.csv", index=False)

print("Cleaned dataset saved.")
