import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import os

# Load data
df = pd.read_csv("review_data/sentiment_reviews.csv")

# Limit to English reviews and drop nulls
df.dropna(subset=['review'], inplace=True)

# Extract keywords using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', max_features=50)
X = vectorizer.fit_transform(df['review'])

# Add keywords to a DataFrame
keywords = vectorizer.get_feature_names_out()
scores = X.toarray().sum(axis=0)

# Store keywords and scores
keywords_df = pd.DataFrame({'keyword': keywords, 'score': scores})
keywords_df = keywords_df.sort_values(by='score', ascending=False)

# Save output
os.makedirs("outputs", exist_ok=True)
keywords_df.to_csv("outputs/top_keywords.csv", index=False)

print("✅ Top keywords saved to outputs/top_keywords.csv")