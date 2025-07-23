import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
try:
    model = joblib.load("esg_rf_model.joblib")
except Exception as e:
    st.error(f"Model could not be loaded. Error: {e}")
    st.stop()

st.title("🌱 ESG Score Predictor for Companies")

st.markdown("Provide the company details below to estimate its ESG score (Environmental, Social, Governance).")

# User input form
with st.form("esg_form"):
    sector = st.selectbox("Sector", ['Finance', 'Energy', 'Technology', 'Healthcare', 'Utilities', 'Retail', 'Other'])
    country = st.selectbox("Country", ['USA', 'India', 'Germany', 'Japan', 'Canada', 'Other'])
    revenue = st.number_input("Annual Revenue (in Million USD)", min_value=1.0, max_value=100000.0, value=500.0, step=10.0)
    employees = st.number_input("Number of Employees", min_value=10, max_value=100000, value=500)
    waste_emissions = st.number_input("Waste Emissions (in tons)", min_value=0.0, value=10.0)
    energy_consumption = st.number_input("Energy Consumption (in MWh)", min_value=0.0, value=100.0)
    water_usage = st.number_input("Water Usage (in KL)", min_value=0.0, value=50.0)
    sustainability_report = st.selectbox("Published Sustainability Report?", ['Yes', 'No'])

    submitted = st.form_submit_button("Predict ESG Score")

if submitted:
    try:
        input_data = pd.DataFrame([{
            'Sector': sector,
            'Country': country,
            'Revenue': revenue,
            'Employees': employees,
            'WasteEmissions': waste_emissions,
            'EnergyConsumption': energy_consumption,
            'WaterUsage': water_usage,
            'SustainabilityReport': sustainability_report
        }])

        # Predict
        prediction = model.predict(input_data)[0]
        st.success(f"Estimated ESG Score: **{prediction:.2f}**")

        if prediction >= 75:
            st.markdown("🟢 The company shows **strong ESG performance**.")
        elif prediction >= 50:
            st.markdown("🟡 The company has **moderate ESG performance**.")
        else:
            st.markdown("🔴 The company needs to **improve its ESG practices**.")

    except Exception as e:
        st.error(f"Prediction failed. Error: {e}")
