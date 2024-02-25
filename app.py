import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open('Customer_Churn_Prediction.pkl', 'rb'))

# Function to make predictions
def predict_churn(CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, Geography, Gender):
    # Convert Geography to one-hot encoding
    if Geography == 'Germany':
        Geography_Germany, Geography_Spain, Geography_France = 1, 0, 0
    elif Geography == 'Spain':
        Geography_Germany, Geography_Spain, Geography_France = 0, 1, 0
    else:
        Geography_Germany, Geography_Spain, Geography_France = 0, 0, 1

    # Convert Gender to binary
    Gender_Male = 1 if Gender == 'Male' else 0
    Gender_Female = 1 - Gender_Male

    # Make prediction
    prediction = model.predict([[CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard,
                                 IsActiveMember, EstimatedSalary, Geography_Germany, Geography_Spain, Gender_Male]])

    return prediction

# Streamlit UI
def main():
    st.title("Customer Churn Prediction")
    st.sidebar.header("User Input")

    # Get user inputs
    CreditScore = st.sidebar.slider("Credit Score", 300, 850, 500)
    Age = st.sidebar.slider("Age", 18, 100, 30)
    Tenure = st.sidebar.slider("Tenure", 0, 10, 5)
    Balance = st.sidebar.slider("Balance", 0.0, 250000.0, 50000.0)
    NumOfProducts = st.sidebar.slider("Number of Products", 1, 4, 2)
    HasCrCard = st.sidebar.selectbox("Has Credit Card", [0, 1])
    IsActiveMember = st.sidebar.selectbox("Is Active Member", [0, 1])
    EstimatedSalary = st.sidebar.slider("Estimated Salary", 0.0, 250000.0, 50000.0)
    Geography = st.sidebar.selectbox("Geography", ["Germany", "Spain", "France"])
    Gender = st.sidebar.selectbox("Gender", ["Male", "Female"])

    # Make prediction
    result = predict_churn(CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember,
                           EstimatedSalary, Geography, Gender)

    # Display result
    if result == 1:
        st.error("The Customer will leave the bank")
    else:
        st.success("The Customer will not leave the bank")

if __name__ == '__main__':
    main()
