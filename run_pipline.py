# run_pipeline.py

from src.data_ingestion import fetch_housing_data, load_housing_data

DOWNLOAD_URL = "https://github.com/ageron/data/raw/main/housing.tgz"
TARBALL_PATH = "data/housing.tgz"
EXTRACT_PATH = "data/"
CSV_PATH = "data/housing/housing.csv"

if __name__ == "__main__":
    fetch_housing_data(DOWNLOAD_URL, TARBALL_PATH, EXTRACT_PATH)
    df = load_housing_data(CSV_PATH)
    print(df.head())
