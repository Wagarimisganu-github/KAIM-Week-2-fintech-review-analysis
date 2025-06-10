# Run the full pipeline step-by-step
from scripts.scrape_reviews import run_scraper
from scripts.preprocess_reviews import clean_data
from scripts.sentiment_analysis import analyze_sentiment
from scripts.theme_extraction import extract_themes

run_scraper()
clean_data()
analyze_sentiment()
extract_themes()