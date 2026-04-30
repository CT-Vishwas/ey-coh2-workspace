import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("House Prices India Dashboard")

# ETL Pipeline

## Extract
@st.cache_data
def extract_data():
    """Load data from CSV file."""
    data = pd.read_csv('../data/house_prices_india.csv')
    return data

data = extract_data()

## Transform
def transform_data(df):
    """Perform basic data transformations."""
    # Fill missing bathrooms with 0 and convert to int
    df = df.copy()
    df['number of bathrooms'] = df['number of bathrooms'].fillna(0).astype(int)
    return df

transformed_data = transform_data(data)

## Load / Display
st.header("Data Overview")
st.subheader("Raw Data Sample")
st.dataframe(transformed_data.head())

# Create a sidebar for filtering
st.sidebar.header("Filter Options")
postal_codes = transformed_data['Postal Code'].unique()
selected_postal_code = st.sidebar.selectbox("Select Postal Code", options=postal_codes)

# Filter data based on selected postal code
filtered_data = transformed_data[transformed_data['Postal Code'] == selected_postal_code]

st.subheader("Data Summary")
st.write(filtered_data.describe())

st.subheader("Data Info")
buffer = filtered_data.info(buf=None)
st.text(buffer)

# Visualizations
st.header("Visualizations")

# Distribution of Bedrooms
st.subheader("Distribution of Number of Bedrooms")
bedroom_counts = filtered_data['number of bedrooms'].value_counts()
fig1, ax1 = plt.subplots(figsize=(6, 6))
ax1.pie(bedroom_counts, labels=bedroom_counts.index, autopct='%1.1f%%', startangle=90)
ax1.set_title('Distribution of Number of Bedrooms')
ax1.axis('equal')
st.pyplot(fig1)

# Average Number of Schools Nearby by Top Postal Codes
st.subheader("Average Number of Schools Nearby by Postal Code (Top 5)")
top_postal_codes = filtered_data.groupby('Postal Code')['Number of schools nearby'].mean().sort_values(ascending=False).head(5)
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x=top_postal_codes.index, y=top_postal_codes.values, ax=ax2)
ax2.set_title('Average Number of Schools Nearby by Postal Code (Top 5)')
ax2.set_xlabel('Postal Code')
ax2.set_ylabel('Average Number of Schools Nearby')
ax2.tick_params(axis='x', rotation=45)
st.pyplot(fig2)

# Average Price by Postal Code (Top 10)
st.subheader("Average Price by Postal Code (Top 10)")
avg_price_postal = filtered_data.groupby('Postal Code')['Price'].mean().sort_values(ascending=False).head(10)
st.bar_chart(avg_price_postal)