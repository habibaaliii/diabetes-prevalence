# Sugar Consumption and Diabetes Prediction

## Project Overview

This project explores the relationship between sugar consumption patterns and the prevalence of diabetes using machine learning techniques. The model is trained to predict **Diabetes Prevalence (%)** from variables such as daily sugar intake, per capita consumption, total consumption, and import/export ratios. The final model is deployed as a Flask-based web application allowing users to interactively input data and receive predictions.

---

## Objective

- Analyze sugar consumption data.
- Predict diabetes prevalence based on consumption patterns.
- Build and compare multiple regression models.
- Deploy the best-performing model in a simple web application.

---

## Dataset Description

The dataset contains 100 observations and 5 features:

| Feature Name                  | Description                                                              |
|------------------------------|--------------------------------------------------------------------------|
| Avg_Daily_Sugar_Intake       | Average daily per capita sugar intake (in grams).                        |
| Per_Capita_Sugar_Consumption | Annual per capita sugar consumption (in kilograms).                      |
| Total_Sugar_Consumption      | Total sugar consumption regionally or nationally (in metric tons).       |
| Sugar_Import_Export_Ratio    | Ratio of imported to exported sugar.                                     |
| Diabetes_Prevalence          | **Target** - Percentage of population with diabetes.                     |

---

## Data Preprocessing

- Checked data types and confirmed all columns are numeric.
- Verified there are no missing or duplicate values.
- Verified columns are correctly named and formatted.
- Analyzed distributions and chose to retain natural outliers.

---

## Exploratory Data Analysis (EDA)

EDA included:

- Histograms and KDE plots for distributions.
- Boxplots to examine spread and outliers.
- Scatter plots and correlation heatmaps to detect linear relationships.
- Summary statistics (mean, std, skewness, etc.).
- Notable Finding: **Avg_Daily_Sugar_Intake** showed strong positive correlation with diabetes prevalence.

---

## 🔍 Feature Selection

- Used **SelectKBest** with the Chi-squared (χ²) test.
- Retained the top features contributing most to the prediction.
- No feature engineering was necessary due to the simplicity and quality of the dataset.

---

## Machine Learning Models

Three models were trained and compared:

| Model                | Description                                                     |
|---------------------|-----------------------------------------------------------------|
| Linear Regression    | Baseline model for comparison.                                 |
| K-Nearest Neighbors  | Non-parametric model using neighborhood-based predictions.     |
| Random Forest        | Ensemble model providing the best performance.                 |

---

## Model Tuning & Evaluation

- **Random Forest** was tuned using `GridSearchCV` and cross-validation.
- Evaluation metrics used:
  - R-squared (R²)
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)
- **Random Forest Regressor** outperformed others and was selected for deployment.

---

## Deployment (Flask App)

The finalized model is deployed using Flask.

### Files:

- `app.py` – Main Flask backend.
- `diabetes_model.pkl` – Serialized trained model.
- `templates/index.html` – HTML input form for user interface.

### User Flow:

1. User inputs sugar data via the web form.
2. Flask loads the model and makes a prediction.
3. Prediction of diabetes prevalence is displayed.

---

## Getting Started

###  Prerequisites

Install required packages:

```bash
pip install pandas numpy scikit-learn flask matplotlib seaborn
