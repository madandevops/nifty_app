# app.py

import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import streamlit as st

# Set page title
st.title("📈 Nifty Stocks Viewer")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('Nifty_Stocks.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

# Select Category
categories = df['Category'].unique()
selected_category = st.selectbox("Select a Category", categories)

# Filter by selected category
filtered_df = df[df['Category'] == selected_category]

# Select Symbol
symbols = filtered_df['Symbol'].unique()
selected_symbol = st.selectbox("Select a Symbol", symbols)

# Filter by selected symbol
stock_data = filtered_df[filtered_df['Symbol'] == selected_symbol]

# Plotting
fig, ax = plt.subplots(figsize=(12, 6))
sb.lineplot(data=stock_data, x='Date', y='Close', ax=ax)
ax.set_title(f'{selected_symbol} Stock Price Over Time')
ax.set_xlabel("Date")
ax.set_ylabel("Closing Price")
plt.xticks(rotation=45)
st.pyplot(fig)
