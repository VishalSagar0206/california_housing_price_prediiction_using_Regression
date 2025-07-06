import streamlit as st
import pandas as pd
import joblib
import os

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
