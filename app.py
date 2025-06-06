
import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('diabetes_model-2.pkl')


# Title
st.title('Diabetes Prevalence Predictor')

# Description
st.write("Enter the following data to predict diabetes prevalence:")

# Input fields for the user
avg_daily_sugar = st.number_input("Avg Daily Sugar Intake (g)", min_value=0.0, step=1.0)
per_capita_sugar = st.number_input("Per Capita Sugar Consumption (kg/year)", min_value=0.0, step=1.0)
total_sugar = st.number_input("Total Sugar Consumption (tonnes)", min_value=0.0, step=100.0)
import_export_ratio = st.number_input("Sugar Import/Export Ratio", min_value=0.0, step=0.1)

# Prediction button
if st.button("Predict"):
    # Make DataFrame for input
    input_data = pd.DataFrame([[avg_daily_sugar, per_capita_sugar, total_sugar, import_export_ratio]],
                               columns=['Avg_Daily_Sugar_Intake', 'Per_Capita_Sugar_Consumption',
                                        'Total_Sugar_Consumption', 'Sugar_Import_Export_Ratio'])
    
    # Predict using the model
    prediction = model.predict(input_data)[0]
    
    # Show result
    st.success(f"Predicted Diabetes Prevalence: {prediction:.2f}%")
