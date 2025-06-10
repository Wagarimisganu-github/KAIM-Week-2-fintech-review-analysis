import pandas as pd
import os

# Load cleaned sentiment reviews
reviews_df = pd.read_csv("review_data/sentiment_reviews.csv")

# Load keyword-theme mapping
keywords_df = pd.read_csv("outputs/keywords_with_themes.csv")
keywords_df.columns = keywords_df.columns.str.strip()  # 👈 removes spaces from column names

# Convert to dictionary: keyword → theme
keyword_theme_map = dict(zip(keywords_df['keyword'], keywords_df['theme']))

# Lowercase for matching
reviews_df['review'] = reviews_df['review'].astype(str).str.lower()

# Function to find matching themes
def match_theme(text):
    matched_themes = set()
    for keyword, theme in keyword_theme_map.items():
        if keyword.lower() in text:
            matched_themes.add(theme)
    return ", ".join(matched_themes) if matched_themes else "Uncategorized"

# Apply to reviews
reviews_df['themes'] = reviews_df['review'].apply(match_theme)

# Save the result
os.makedirs("review_data", exist_ok=True)
reviews_df.to_csv("review_data/sentiment_reviews_with_themes.csv", index=False)

print(f"✅ Reviews tagged with themes. Saved to review_data/sentiment_reviews_with_themes.csv")