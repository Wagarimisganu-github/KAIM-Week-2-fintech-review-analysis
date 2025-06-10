from google_play_scraper import reviews, Sort
import pandas as pd
import os

# Bank apps and their package names
apps = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.cr2.amolelight"
}

# Ensure output folder exists
os.makedirs("review_data", exist_ok=True)

for bank, app_id in apps.items():
    print(f"Scraping {bank} reviews...")
    
    result, _ = reviews(
        app_id,
        lang='en',
        country='us',
        sort=Sort.NEWEST,
        count=400  # Minimum required
    )

    df = pd.DataFrame(result)[['content', 'score', 'at']]
    df.rename(columns={
        'content': 'review',
        'score': 'rating',
        'at': 'date'
    }, inplace=True)
    df['bank'] = bank
    df['source'] = 'Google Play'
    
    file_path = f"review_data/{bank.lower()}_reviews.csv"
    df.to_csv(file_path, index=False)
    print(f"✅ Saved {len(df)} reviews to {file_path}")