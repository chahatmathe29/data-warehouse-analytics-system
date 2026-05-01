import streamlit as st
import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql2005",
    database="expense_dw"
)

df = pd.read_sql("SELECT * FROM transactions", conn)

st.title("💸 Expense Dashboard")

st.subheader("Category Spending")
category_spend = df.groupby('category')['amount'].sum()
st.bar_chart(category_spend)

df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month

monthly = df.groupby('month')['amount'].sum()

st.subheader("Monthly Trend")
st.line_chart(monthly)

conn.close()