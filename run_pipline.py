from src.data_ingestion import fetch_housing_data, load_housing_data
from src.data_preprocessing import split_data, build_preprocessing_pipeline
from src.model_training import train_model, save_model
from src.model_evaluation import load_artifacts, evaluate_model

DOWNLOAD_URL = "https://github.com/ageron/data/raw/main/housing.tgz"
TARBALL_PATH = "data/housing.tgz"
EXTRACT_PATH = "data/"
CSV_PATH = "data/housing/housing.csv"

if __name__ == "__main__":
    # Step 1: Data Ingestion
    fetch_housing_data(DOWNLOAD_URL, TARBALL_PATH, EXTRACT_PATH)
    df = load_housing_data(CSV_PATH)

    # Step 2: Train-test Split
    train_set, test_set = split_data(df)

    # Step 3: Preprocessing on train
    X_train_prepared, y_train, pipeline = build_preprocessing_pipeline(train_set)

    # Step 4: Train model
    model = train_model(X_train_prepared, y_train)

    # Step 5: Save model & pipeline
    save_model(model, pipeline)

    # Step 6: Load & Evaluate
    model_loaded, pipeline_loaded = load_artifacts()
    rmse, r2 = evaluate_model(model_loaded, pipeline_loaded, test_set)

    print("✅ Model evaluation complete!")
    print(f"RMSE: {rmse:.2f}")
    print(f"R² Score: {r2:.4f}")
