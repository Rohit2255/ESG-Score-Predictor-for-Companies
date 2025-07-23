# 🌱 ESG Score Predictor for Companies using Machine Learning

This project predicts a company's ESG (Environmental, Social, Governance) score using machine learning models. ESG scores are widely used to assess the sustainability and ethical impact of a company — making them crucial in modern investment decisions and financial analytics.

---

## 📊 Problem Statement

Many companies publish sustainability reports, and some regions require ESG disclosures. However, there's still inconsistency in the availability and transparency of ESG scores across countries and sectors.

**Goal:** Build a machine learning pipeline that predicts ESG scores using company-level features like sector, country, sustainability report status, etc.

---

## 🗂️ Dataset Overview

The dataset consists of anonymized company information and their associated ESG scores.

### Features used:
- `Company` (Dropped for training)
- `Sector` (Categorical)
- `Country` (Categorical)
- `Revenue` (Numeric)
- `EmployeeCount` (Numeric)
- `MarketCap` (Numeric)
- `SustainabilityReport` (Categorical: Yes/No)
- `ESGScore` (Target Variable - numeric)

---

## 🧪 Project Steps

### 1. 📦 Data Preprocessing

- Dropped `Company` column (non-informative)
- Split into features (`X`) and target (`y = ESGScore`)
- Identified:
  - **Categorical features**: `Sector`, `Country`, `SustainabilityReport`
  - **Numerical features**: All other remaining columns
- Applied a `ColumnTransformer` to:
  - Standard scale numerical columns
  - One-hot encode categorical columns

### 2. 🔨 Model Pipeline

- Used `Pipeline` from `sklearn` to combine preprocessing and model training
- Model used: `RandomForestRegressor` with `n_estimators=100`
- Split data: 80% training / 20% testing

### 3. 📈 Evaluation Metrics

After training, the model was evaluated on test data using:

- **R² Score**: Goodness of fit
- **Mean Absolute Error (MAE)**: Average error magnitude
- **Root Mean Squared Error (RMSE)**: Penalizes large errors

```python
Random Forest R² Score: 0.85+
MAE: ~2.5
RMSE: ~3.2
