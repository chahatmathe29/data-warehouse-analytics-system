import pandas as pd
import mysql.connector
from sklearn.linear_model import LinearRegression

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql2005",
    database="expense_dw"
)

df = pd.read_sql("SELECT * FROM transactions", conn)

df['date'] = pd.to_datetime(df['date'])
df['day'] = df['date'].dt.day

X = df[['day']]
y = df['amount']

model = LinearRegression()
model.fit(X, y)

future_days = [[28], [29], [30], [31], [32]]
predictions = model.predict(future_days)

print("Predictions:")
for d, p in zip(future_days, predictions):
    print(f"Day {d[0]} → ₹{round(p,2)}")

conn.close()