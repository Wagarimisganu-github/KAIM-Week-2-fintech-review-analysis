import pandas as pd
import os

# Input files
banks = ['cbe', 'boa', 'dashen']
dataframes = []

for bank in banks:
    path = f"review_data/{bank}_reviews.csv"
    df = pd.read_csv(path)
    df['bank'] = bank.upper()
    dataframes.append(df)

# Merge all banks
all_reviews = pd.concat(dataframes, ignore_index=True)

# Drop duplicates & NaNs
all_reviews.drop_duplicates(subset='review', inplace=True)
all_reviews.dropna(subset=['review', 'rating', 'date'], inplace=True)

# Format date
all_reviews['date'] = pd.to_datetime(all_reviews['date']).dt.date

# Save cleaned dataset
os.makedirs("review_data", exist_ok=True)
all_reviews.to_csv("review_data/cleaned_reviews.csv", index=False)

print(f"✅ Cleaned data saved to review_data/cleaned_reviews.csv with {len(all_reviews)} rows.")