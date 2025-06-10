import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os

# Load cleaned reviews
df = pd.read_csv("review_data/cleaned_reviews.csv")

# Initialize VADER
analyzer = SentimentIntensityAnalyzer()

# Function to classify sentiment
def get_sentiment(text):
    score = analyzer.polarity_scores(text)['compound']
    if score >= 0.05:
        return "positive", score
    elif score <= -0.05:
        return "negative", score
    else:
        return "neutral", score

# Apply sentiment
df[['sentiment_label', 'sentiment_score']] = df['review'].apply(lambda x: pd.Series(get_sentiment(str(x))))

# Save results
df.to_csv("review_data/sentiment_reviews.csv", index=False)
print(f"✅ Sentiment results saved to review_data/sentiment_reviews.csv with {len(df)} rows.")