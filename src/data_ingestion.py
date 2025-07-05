# src/data_ingestion.py

from pathlib import Path
import pandas as pd
import tarfile
import urllib.request

def fetch_housing_data(download_url, download_path, extract_path):
    """Download and extract housing dataset."""
    tarball_path = Path(download_path)
    if not tarball_path.is_file():
        Path(download_path).parent.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(download_url, tarball_path)
    with tarfile.open(tarball_path) as tar_file:
        tar_file.extractall(path=extract_path)

def load_housing_data(csv_path):
    """Load the dataset into a DataFrame."""
    return pd.read_csv(Path(csv_path))
