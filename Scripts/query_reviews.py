import pandas as pd
import cx_Oracle

# Establish Oracle DB connection
connection = cx_Oracle.connect(
    user="bank_reviews",
    password="Bank123!",
    dsn="localhost:1521/XEPDB1"
)

# Define your SQL query
query = "SELECT * FROM reviews"

# Read from Oracle DB into pandas DataFrame
df = pd.read_sql(query, con=connection)

# Optional: Standardize column names to lowercase for easier access
df.columns = df.columns.str.lower()

# If needed: convert 'review_text' to string
df['review_text'] = df['review_text'].astype(str)

# Export to CSV
df.to_csv("outputs/reviews_from_db.csv", index=False)

# Close the DB connection
connection.close()