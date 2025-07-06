# src/model_evaluation.py

from sklearn.metrics import mean_squared_error, r2_score
import joblib
from pathlib import Path
import numpy as np

def load_artifacts(model_path="artifacts/model.pkl", pipeline_path="artifacts/pipeline.pkl"):
    model = joblib.load(Path(model_path))
    pipeline = joblib.load(Path(pipeline_path))
    return model, pipeline

def evaluate_model(model, pipeline, df_test):
    df = df_test.copy()
    df.dropna(subset=["median_house_value", "total_bedrooms"], inplace=True)

    y_true = df["median_house_value"].copy()
    X = df.drop("median_house_value", axis=1)

    X_prepared = pipeline.transform(X)
    y_pred = model.predict(X_prepared)

    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)

    return rmse, r2
