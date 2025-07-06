import streamlit as st
import pandas as pd
import joblib
import os

@st.cache_resource
def load_artifacts():
    model = joblib.load(os.path.join("artifacts", "model.pkl"))
    pipeline = joblib.load(os.path.join("artifacts", "pipeline.pkl"))
    return model, pipeline

model, pipeline = load_artifacts()
