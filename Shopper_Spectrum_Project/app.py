# ==============================
# Basic Streamlit Setup
# ==============================

import os
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics.pairwise import cosine_similarity


# ==============================
# Dataset Availability Check
# ==============================

DATA_PATH = "data/online_retail.csv"

if not os.path.exists(DATA_PATH):
    st.error(
        "Dataset not found.\n\n"
        "Please download 'online_retail.csv' from the dataset link "
        "mentioned in the README and place it inside:\n\n"
        "Shopper_Spectrum_Project/data/"
    )
    st.stop()


# ==============================
# Load Models & Data
# ==============================

kmeans = joblib.load("models/kmeans_model.pkl")
scaler = joblib.load("models/scaler.pkl")

data = pd.read_csv(DATA_PATH)

# Lightweight preprocessing (runtime-safe)
data = data.dropna(subset=["CustomerID", "Description"])
data = data[(data["Quantity"] > 0) & (data["UnitPrice"] > 0)]


# ==============================
# Build Recommendation Logic
# ==============================

customer_product_matrix = data.pivot_table(
    index="CustomerID",
    columns="Description",
    values="Quantity",
    aggfunc="sum",
    fill_value=0
)

product_customer_matrix = customer_product_matrix.T
product_similarity = cosine_similarity(product_customer_matrix)

product_similarity_df = pd.DataFrame(
    product_similarity,
    index=product_customer_matrix.index,
    columns=product_customer_matrix.index
)


# ==============================
# Recommendation Function
# ==============================

def recommend_products(product_name, similarity_df, top_n=5):
    product_name = product_name.upper()
    similarity_df.index = similarity_df.index.str.upper()

    if product_name not in similarity_df.index:
        return []

    scores = similarity_df[product_name].sort_values(ascending=False)
    return scores.iloc[1:top_n + 1].index.tolist()


# ==============================
# Streamlit UI – Product Recommendation
# ==============================

st.title("🛒 Shopper Spectrum")

st.caption(
    "Customer Segmentation & Product Recommendation System "
    "using RFM Analysis and Collaborative Filtering"
)

st.header("🎯 Product Recommendation")

product_input = st.text_input("Enter Product Name")

if st.button("Get Recommendations"):
    recommendations = recommend_products(
        product_input,
        product_similarity_df
    )

    if recommendations:
        st.subheader("Top 5 Recommended Products:")
        for prod in recommendations:
            st.write(f"- {prod}")
    else:
        st.warning("Product not found in the dataset.")


# ==============================
# Streamlit UI – Customer Segmentation
# ==============================

st.header("👤 Customer Segmentation")

segment_map = {
    0: "Occasional",
    1: "At-Risk",
    2: "High-Value",
    3: "Regular"
}

recency = st.number_input("Recency (days)", min_value=0)
frequency = st.number_input("Frequency", min_value=0)
monetary = st.number_input("Monetary Value", min_value=0.0)

if st.button("Predict Customer Segment"):
    if recency == 0 and frequency == 0 and monetary == 0:
        st.warning("Please enter valid RFM values.")
    else:
        input_data = np.array([[recency, frequency, monetary]])
        input_scaled = scaler.transform(input_data)
        cluster = kmeans.predict(input_scaled)[0]
        st.success(f"Customer Segment: {segment_map.get(cluster)}")
