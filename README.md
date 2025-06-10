# 📊 KAIM Week 2: Fintech Review Analysis

This project analyzes customer reviews of mobile banking apps from three major Ethiopian banks — **Commercial Bank of Ethiopia (CBE)**, **Bank of Abyssinia (BOA)**, and **Dashen Bank** — on the Google Play Store. The goal is to extract actionable insights on user satisfaction and pain points using sentiment and thematic analysis.

---

## 🚀 Business Context

Omega Consultancy is supporting these banks to improve their mobile applications by:
- Identifying what users like (drivers) and dislike (pain points)
- Improving app features, UI/UX, and support systems
- Retaining users and increasing satisfaction

---

## 🔧 Tools and Libraries

| Tool/Library         | Purpose                               |
|----------------------|----------------------------------------|
| `pandas`             | Data manipulation and preprocessing    |
| `TextBlob`           | Sentiment analysis                     |
| `matplotlib` / `seaborn` | Visualization                    |
| `wordcloud`          | Word cloud generation                  |
| `scikit-learn`       | TF-IDF keyword extraction              |
| `google-play-scraper`| App review scraping (Python)          |
| `pytest`             | Unit testing                           |

---

## 📁 Folder Structure

KAIM-Week-2-fintech-review-analysis/
│
├── Scripts/
│ ├── scrape_reviews.py # Scrapes reviews using Google Play Scraper
│ ├── preprocess_reviews.py # Cleans and prepares text
│ ├── sentiment_analysis.py # Assigns sentiment scores
│ ├── theme_extraction.py # Extracts and clusters themes
│
├── notebooks/
│ ├── analysis.ipynb # EDA and insights
│ ├── visual_analysis.ipynb # Plots and visualizations
│ └── run_analysis.py # Executes full pipeline
│
├── review_data/
│ ├── cbe_reviews.csv
│ ├── boa_reviews.csv
│ └── dashen_reviews.csv # Cleaned reviews per bank
│
├── outputs/
│ ├── keyword_cloud.png
│ ├── sentiment_plot.png
│ ├── comparison_chart.png
│ ├── top_keywords.csv
│ └── visualizations.zip # Zipped visual outputs
│
├── tests/
│ └── test_sentiment.py # Unit test for sentiment logic
│
├── reports/
│ └── interim_report.pdf
│
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## 🛠️ How to Run

### 1. 🔁 Run Entire Pipeline

```bash
python notebooks/run_analysis.py
This runs:

scrape_reviews.py

preprocess_reviews.py

sentiment_analysis.py

theme_extraction.py

2. 📊 Generate Visuals
Open visual_analysis.ipynb and run all cells to:

View theme-based sentiment distribution

Bank-wise sentiment chart

Keyword cloud

3. 🧪 Run Tests
bash
Copy
Edit
pytest tests/test_sentiment.py
📌 Key Outcomes
Sentiment Scores calculated for all reviews

Themes like "login issues", "slow transfer", "good UI" identified

Insights visualized via bar charts and word clouds

Interim Report delivered with 2-page analysis in /reports/

📅 Project Milestones
✅ Task 1: Data scraping + cleaning

✅ Task 2: Sentiment and thematic analysis

⏳ Task 3: Oracle DB storage (next)

⏳ Task 4: Final report with recommendations

🧠 Contributors
Facilitated by the KAIM AI Mastery Program. Built by: Rufael Eshetu

📄 License
This project is for academic use under the 10 Academy AI Mastery Week 2 challenge.

yaml
Copy
Edit

---

✅ Once you save this to `README.md`, commit and push:

```bash
git add README.md
git commit -m "Add complete README with overview, structure, and usage"
git push origin main