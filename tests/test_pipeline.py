import os
import joblib
import pandas as pd

def test_artifacts_exist():
    assert os.path.exists("artifacts/model.pkl"), "model.pkl not found"
    assert os.path.exists("artifacts/pipeline.pkl"), "pipeline.pkl not found"

def test_model_prediction():
    model = joblib.load("artifacts/model.pkl")
    pipeline = joblib.load("artifacts/pipeline.pkl")

    sample = pd.DataFrame([{
        "longitude": -118.0,
        "latitude": 34.0,
        "housing_median_age": 20,
        "total_rooms": 1500,
        "total_bedrooms": 300,
        "population": 800,
        "households": 300,
        "median_income": 6.0,
        "ocean_proximity": "NEAR OCEAN"
    }])

    X_prepared = pipeline.transform(sample)
    prediction = model.predict(X_prepared)

    assert prediction.shape == (1,), "Model should return one prediction"
