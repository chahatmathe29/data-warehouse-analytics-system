import pandas as pd
import mysql.connector

df = pd.read_csv("data/expenses.csv")
df['date'] = pd.to_datetime(df['date'])

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql2005",
    database="expense_dw"
)

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute(
        "INSERT INTO transactions (date, category, amount) VALUES (%s, %s, %s)",
        (row['date'], row['category'], row['amount'])
    )

conn.commit()
conn.close()

print("ETL Done ✅")