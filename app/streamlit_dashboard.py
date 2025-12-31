import streamlit as st
from utils import predict_fraud

st.title("💳 Fraud Detection Dashboard")

amount = st.number_input("Enter transaction amount:", min_value=0.0)
location = st.text_input("Enter location:")
card_type = st.selectbox("Select card type:", ["Debit", "Credit"])

if st.button("Check Transaction"):
    try:
        result = predict_fraud(amount, location, card_type)
        if "Fraudulent" in result:
            st.error(f"⚠️ ALERT: {result}")
        else:
            st.success(f"✅ {result}")
    except Exception as e:
        st.warning(f"Error: {e}. Make sure the location exists in training data.")
