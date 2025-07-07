import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("demand_model.pkl")

# App title
st.title("📦 AI-Based Demand Forecasting App")

st.markdown("Enter the product features below to predict demand:")

# Input fields
product_code = st.selectbox("Product ID", [0, 1, 2], format_func=lambda x: f"P00{x+1}")
past_demand = st.number_input("Past Demand", min_value=50, max_value=150, value=100)
price = st.number_input("Price", min_value=10, max_value=50, value=20)
promotion = st.selectbox("Promotion Applied?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

# Predict button
if st.button("Predict Demand"):
    input_data = np.array([[past_demand, price, promotion, product_code]])
    prediction = model.predict(input_data)[0]
    st.success(f"📈 Predicted Demand: **{round(prediction)} units**")
