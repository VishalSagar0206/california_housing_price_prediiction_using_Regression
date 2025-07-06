# src/data_preprocessing.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

def split_data(df, test_size=0.2, random_state=42):
    """
    Split the dataset into training and testing sets.
    """
    return train_test_split(df, test_size=test_size, random_state=random_state)

def build_preprocessing_pipeline(df):
    """
    Build preprocessing pipeline for numerical and categorical features.
    Returns:
        X_train_prepared: Preprocessed feature matrix
        y_train: Target values
        full_pipeline: Pipeline object (for reuse on test set or new data)
    """
    df = df.copy()

    # Drop rows with missing values in either features or label
    df.dropna(subset=["median_house_value", "total_bedrooms"], inplace=True)

    # Separate label
    y = df["median_house_value"].copy()
    df.drop("median_house_value", axis=1, inplace=True)

    # Identify columns
    num_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    cat_cols = df.select_dtypes(include=["object"]).columns.tolist()

    # Numerical pipeline
    num_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    # Full pipeline: numeric + categorical
    full_pipeline = ColumnTransformer([
        ("num", num_pipeline, num_cols),
        ("cat", OneHotEncoder(), cat_cols)
    ])

    # Fit & transform
    X_prepared = full_pipeline.fit_transform(df)

    return X_prepared, y, full_pipeline
