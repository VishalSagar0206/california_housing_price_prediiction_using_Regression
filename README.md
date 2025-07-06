# California Housing Price Prediction

An end-to-end machine learning pipeline to predict California housing prices using regression. This project is inspired by the Hands-On Machine Learning book and follows best practices for modular, production-ready ML code.

## Project Highlights

- Data ingestion from remote `.tgz` source
- Data preprocessing with Scikit-learn pipelines
- Train-test split, imputation, scaling, and encoding
- Model training using Linear Regression
- Model evaluation using RMSE and R² score
- Artifacts saved using `joblib` (model and pipeline)
- Modular codebase for easy extension and deployment

## Badges

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.2%2B-orange)](https://scikit-learn.org/)
[![License](https://img.shields.io/github/license/VishalSagar0206/california_housing_price_prediiction_using_Regression)](./LICENSE)

## Project Structure

housing_price_using_regression/
├── artifacts/ # Saved model and pipeline
├── data/ # Raw and extracted data
├── notebooks/ # Jupyter notebooks
├── src/ # Source code modules
│ ├── data_ingestion.py
│ ├── data_preprocessing.py
│ ├── model_training.py
│ └── model_evaluation.py
├── run_pipeline.py # Main entrypoint to execute pipeline
├── requirements.txt
└── README.md

## How to Run This Project

1. **Clone the repository**
   ```bash
   git clone git@github.com:VishalSagar0206/california_housing_price_prediiction_using_Regression.git
   cd california_housing_price_prediiction_using_Regression

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python run_pipeline.py

Trained model: artifacts/model.pkl

Preprocessing pipeline: artifacts/pipeline.pkl

| Metric | Value (sample run) |
| ------ | ------------------ |
| RMSE   | \~69000            |
| R²     | \~0.64             |


---

## STEP 2: Add LICENSE File (MIT)

Run:

```bash
touch LICENSE
nano LICENSE


## Live Demo

Try the app here:[California Housing Price Predictor](https://californiahousingpriceprediictionusingregression-jrh34d4nhpbss.streamlit.app)
