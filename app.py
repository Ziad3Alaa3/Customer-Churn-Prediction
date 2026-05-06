import streamlit as st
import pandas as pd
import joblib


@st.cache_resource
def load_model():
    """Load the trained machine learning pipeline."""
    return joblib.load("churn_prediction_pipeline.pkl")


model = load_model()

st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📉",
    layout="centered"
)

st.title("📉 Customer Churn Prediction App")

st.write(
    "This app predicts whether a customer is likely to churn based on "
    "customer profile, contract details, and payment behavior."
)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Customer Information")

    age = st.number_input(
        "Customer Age",
        min_value=18,
        max_value=100,
        value=30
    )

    tenure = st.number_input(
        "Tenure in Months",
        min_value=1,
        max_value=100,
        value=12
    )

    monthly_charges = st.number_input(
        "Monthly Charges ($)",
        min_value=10.0,
        max_value=200.0,
        value=50.0
    )

with col2:
    st.subheader("Contract Details")

    contract_type = st.selectbox(
        "Contract Type",
        ["Month-to-month", "One year", "Two year"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["Yes", "No"]
    )

st.markdown("---")

if st.button("Predict Churn", use_container_width=True):
    input_data = pd.DataFrame({
        "Age": [age],
        "Tenure_Months": [tenure],
        "Monthly_Charges": [monthly_charges],
        "Contract_Type": [contract_type],
        "Tech_Support": [tech_support]
    })

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ High churn risk: This customer is likely to leave.")
        st.info(
            "Suggested action: Offer a retention discount, improve support, "
            "or encourage the customer to move to a longer-term contract."
        )
    else:
        st.success("✅ Low churn risk: This customer is likely to stay.")
        st.balloons()
