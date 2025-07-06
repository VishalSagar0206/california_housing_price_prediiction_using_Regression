import streamlit as st
import pandas as pd
import joblib

# Load model and pipeline
model = joblib.load("artifacts/model.pkl")
pipeline = joblib.load("artifacts/pipeline.pkl")

st.title("California Housing Price Predictor")

st.markdown("Enter the property details below:")

# Example input form
longitude = st.number_input("Longitude", -125.0, -113.0, -118.0)
latitude = st.number_input("Latitude", 32.0, 43.0, 34.0)
housing_median_age = st.slider("Housing Median Age", 1, 52, 20)
total_rooms = st.number_input("Total Rooms", 1, 10000, 1000)
total_bedrooms = st.number_input("Total Bedrooms", 1, 5000, 300)
population = st.number_input("Population", 1, 10000, 1000)
households = st.number_input("Households", 1, 5000, 400)
median_income = st.number_input("Median Income", 0.0, 20.0, 5.0)
ocean_proximity = st.selectbox("Ocean Proximity", ['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN'])

if st.button("Predict Price"):
    input_df = pd.DataFrame([{
        "longitude": longitude,
        "latitude": latitude,
        "housing_median_age": housing_median_age,
        "total_rooms": total_rooms,
        "total_bedrooms": total_bedrooms,
        "population": population,
        "households": households,
        "median_income": median_income,
        "ocean_proximity": ocean_proximity
    }])

    processed_input = pipeline.transform(input_df)
    prediction = model.predict(processed_input)[0]

    st.success(f"Predicted Median House Value: ${prediction:,.2f}")
