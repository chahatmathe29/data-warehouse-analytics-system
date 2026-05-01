import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql2005",
    database="expense_dw"
)

df = pd.read_sql("SELECT * FROM transactions", conn)

category_spend = df.groupby('category')['amount'].sum()

category_spend.plot(kind='bar')
plt.title("Category-wise Spending")
plt.show()

df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month

monthly = df.groupby('month')['amount'].sum()

monthly.plot(kind='line')
plt.title("Monthly Trend")
plt.show()

conn.close()