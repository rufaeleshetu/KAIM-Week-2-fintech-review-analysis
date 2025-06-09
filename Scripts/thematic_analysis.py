import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.corpus import stopwords

# Ensure stopwords are available
nltk.download('stopwords')
stop_words = stopwords.words('english')

# Load the data
df = pd.read_csv("outputs/reviews_from_db.csv")

# Ensure consistent column names
df.columns = df.columns.str.lower()

# Clean text column (rename to 'clean_text' if it exists differently)
df["clean_text"] = df["review_text"].astype(str).str.lower()

# Vectorize the text
vectorizer = CountVectorizer(stop_words=stop_words, max_df=1.0, min_df=1)
dtm = vectorizer.fit_transform(df["clean_text"])

# Get feature names (i.e., words)
features = vectorizer.get_feature_names_out()

# Convert to DataFrame
dtm_df = pd.DataFrame(dtm.toarray(), columns=features)

# Save for inspection
dtm_df.to_csv("outputs/thematic_matrix.csv", index=False)

print("✅ Thematic matrix saved as outputs/thematic_matrix.csv")