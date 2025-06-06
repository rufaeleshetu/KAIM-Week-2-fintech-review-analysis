# KAIM Week 2 – Fintech Review Analysis

## 📌 Objective
Analyze mobile banking app reviews (CBE, BOA, Dashen) from the Google Play Store to identify sentiment trends, satisfaction drivers, and app improvement recommendations using NLP.

## 🗂️ Project Structure
Scripts/
├── scrape_reviews.py
├── preprocess_reviews.py
├── sentiment_analysis.py
├── theme_extraction.py
notebooks/
├── analysis.ipynb
├── visual_analysis.ipynb
outputs/
├── sentiment_plot.png
├── wordcloud.png
├── comparison_chart.png
reports/
├── interim_report.pdf
review_data/
├── [scraped CSV files]

markdown
Copy
Edit

## ⚙️ How to Run
1. Install dependencies:  
   ```bash
   pip install -r requirements.txt
Run scripts in order:

scrape_reviews.py

preprocess_reviews.py

sentiment_analysis.py

theme_extraction.py

Open visual_analysis.ipynb to explore results.

🧪 Test
bash
Copy
Edit
python tests/test_sentiment.py
👥 Team
Facilitators: Mahlet, Rediet, Kerod, Rehmet
Cohort: KAIM Week 2