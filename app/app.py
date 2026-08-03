import joblib
import numpy as np
import pandas as pd
import streamlit as st
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR.parent / "model" / "best_profit_model.joblib"
model = joblib.load(MODEL_PATH)

CATEGORIES = ["Furniture", "Office Supplies", "Technology"]
REGIONS = ["Central", "East", "South", "West"]

def engineer_features(data):
    data = data.copy()
    data["DiscountAmount"] = data["Sales"] * data["Discount"]
    data["NetSales"] = data["Sales"] * (1 - data["Discount"])
    data["LogSales"] = np.log1p(data["Sales"].clip(lower=0))
    data["HighDiscount"] = (data["Discount"] >= 0.30).astype(int)
    return data

st.title("Superstore Discount Simulator")
st.write("Estimate Profit before approving a discount.")

sales = st.number_input("Sales", min_value=0.0, value=500.0, step=10.0)
discount_percent = st.slider("Discount (%)", min_value=0, max_value=80, value=20)
category = st.selectbox("Category", CATEGORIES)
region = st.selectbox("Region", REGIONS)

if st.button("Predict Profit"):
    raw = pd.DataFrame([{
        "Sales": sales,
        "Discount": discount_percent / 100,
        "Category": category,
        "Region": region,
    }])
    prediction = model.predict(engineer_features(raw))[0]
    st.metric("Estimated Profit", f"${prediction:,.2f}")
    if prediction < 0:
        st.error("Warning: predicted loss-making order.")
    elif discount_percent > 20:
        st.warning("Predicted profitable, but discount exceeds the routine 20% ceiling.")
    else:
        st.success("Predicted profitable and within the routine discount ceiling.")
