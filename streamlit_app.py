import streamlit as st
import pandas as pd
import joblib
import os

# -------------------------------------
# Load Model and Pipeline
# -------------------------------------
@st.cache_resource
def load_artifacts():
    model_path = os.path.join("artifacts", "model.pkl")
    pipeline_path = os.path.join("artifacts", "pipeline.pkl")

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Missing: {model_path}")
    if not os.path.exists(pipeline_path):
        raise FileNotFoundError(f"Missing: {pipeline_path}")

    model = joblib.load(model_path)
    pipeline = joblib.load(pipeline_path)
    return model, pipeline

model, pipeline = load_artifacts()

# -------------------------------------
# App Title and Description
# -------------------------------------
st.set_page_config(page_title="California Housing Price Predictor", layout="wide")
st.title("🏠 California Housing Price Predictor")
st.markdown(
    """
    This app uses a trained regression model to predict the median house value in California based on housing characteristics.
    Enter the details below to see the predicted price. All inputs are based on features from the California Housing Dataset.
    """
)

# -------------------------------------
# Input Form (Two-Column Layout)
# -------------------------------------
with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        longitude = st.number_input("Longitude", -125.0, -113.0, -118.0, step=0.1)
        latitude = st.number_input("Latitude", 32.0, 43.0, 34.0, step=0.1)
        housing_median_age = st.slider("Housing Median Age", 1, 52, 20)
        total_rooms = st.number_input("Total Rooms", 1, 10000, 1000)
        total_bedrooms = st.number_input("Total Bedrooms", 1, 5000, 300)

    with col2:
        population = st.number_input("Population", 1, 10000, 1000)
        households = st.number_input("Households", 1, 5000, 400)
        median_income = st.number_input("Median Income ($k)", 0.0, 20.0, 5.0, step=0.1)
        ocean_proximity = st.selectbox(
            "Ocean Proximity", 
            ['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN']
        )

    submitted = st.form_submit_button("🔍 Predict House Price")

# -------------------------------------
# Prediction Output
# -------------------------------------
if submitted:
    input_data = pd.DataFrame([{
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

    # Preprocess and predict
    processed = pipeline.transform(input_data)
    prediction = model.predict(processed)[0]

    st.markdown("---")
    st.subheader("📊 Prediction Result")
    st.metric(label="Predicted Median House Value", value=f"${prediction:,.2f}")

    st.info("This prediction is based on your input. Prices are in USD.")

# -------------------------------------
# Footer
# -------------------------------------
st.markdown("---")
st.caption("Built by Vishal K · Powered by Scikit-learn · Deployed on Streamlit Cloud")
