import cx_Oracle
import datetime

# Step 1: Establish DB connection
connection = cx_Oracle.connect(
    user="bank_reviews",
    password="Bank123!",
    dsn="localhost/XEPDB1"
)

cursor = connection.cursor()

# Step 2: Sample review data
review_data = [
    ("App is great, love the features", 5, datetime.date.today(), "CBE", "Play Store"),
    ("Crashes too often", 1, datetime.date.today(), "BOA", "Play Store")
]

# Step 3: Insert into `reviews`
for review_text, rating, review_date, bank_name, source in review_data:
    cursor.execute("""
        INSERT INTO reviews (review_text, rating, review_date, bank_name, source)
        VALUES (:1, :2, :3, :4, :5)
    """, (review_text, rating, review_date, bank_name, source))

# Step 4: Commit and clean up
connection.commit()
cursor.close()
connection.close()

print("✅ Sample reviews inserted successfully!")