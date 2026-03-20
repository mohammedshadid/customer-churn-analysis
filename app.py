import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Customer Churn Prediction App")

st.write("Enter customer details:")

# Inputs
tenure = st.slider("Tenure (Months)", 0, 72)
monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0)

contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
payment = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])

tech_support = st.selectbox("Tech Support", ["Yes", "No"])
online_security = st.selectbox("Online Security", ["Yes", "No"])
paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])

# Convert to numeric (IMPORTANT)
data = pd.DataFrame([{
    "tenure": tenure,
    "MonthlyCharges": monthly_charges,
    "Contract_One year": 1 if contract == "One year" else 0,
    "Contract_Two year": 1 if contract == "Two year" else 0,
    "InternetService_Fiber optic": 1 if internet == "Fiber optic" else 0,
    "PaymentMethod_Electronic check": 1 if payment == "Electronic check" else 0,
    "TechSupport_Yes": 1 if tech_support == "Yes" else 0,
    "OnlineSecurity_Yes": 1 if online_security == "Yes" else 0,
    "PaperlessBilling_Yes": 1 if paperless == "Yes" else 0,
    "Dependents_Yes": 1 if dependents == "Yes" else 0
}])

# Predict
if st.button("Predict"):
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Customer is likely to churn")
    else:
        st.success("Customer is not likely to churn")