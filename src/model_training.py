# src/model_training.py

from sklearn.linear_model import LinearRegression
import joblib
from pathlib import Path

def train_model(X_train, y_train):
    """Train and return a Linear Regression model."""
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def save_model(model, pipeline, model_path="artifacts/model.pkl", pipeline_path="artifacts/pipeline.pkl"):
    """Save trained model and preprocessing pipeline."""
    Path("artifacts").mkdir(parents=True, exist_ok=True)
    joblib.dump(model, model_path)
    joblib.dump(pipeline, pipeline_path)
