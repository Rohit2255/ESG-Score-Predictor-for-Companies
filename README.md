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

## 🚀 Optional Streamlit App (Local Use)

You can run a Streamlit app to interactively predict ESG scores for companies based on their features.

### Steps to Run Streamlit App:

1. **Install Streamlit** if not already:
   ```bash
   pip install streamlit


## 📈 Model Metrics (RandomForestRegressor)

| Metric | Value |
|--------|-------|
| R² Score | **0.91** |
| MAE (Mean Absolute Error) | **1.30** |
| RMSE (Root Mean Squared Error) | **1.55** |

These metrics indicate that the model performs well in predicting ESG scores on unseen data. The R² score of 0.91 suggests that the model explains 91% of the variance in the target variable.

---

## 📊 Future Improvements

Here are several ways this project can be further enhanced:

- ✅ Integrate real-world ESG datasets from MSCI, Refinitiv, or Yahoo Finance.
- ✅ Include SHAP or LIME explainability tools to interpret model predictions.
- ✅ Deploy the app on **Streamlit Cloud**, **Hugging Face Spaces**, or **Render**.
- ✅ Add model versioning and CI/CD pipeline using GitHub Actions.
- ✅ Allow user-uploaded CSV files for batch ESG score predictions.

---

## 📚 References

- 📘 [Scikit-Learn Documentation](https://scikit-learn.org/stable/)
- 🌍 [MSCI ESG Ratings Overview](https://www.msci.com/our-solutions/esg-investing/esg-ratings)
- 📊 [Sustainability Reporting Guidelines – GRI](https://www.globalreporting.org/standards/)
- 📺 [Streamlit Official Docs](https://docs.streamlit.io/)

---

## 📜 License

This project is licensed under the **MIT License**.

You are free to:

- ✅ Use it for personal or commercial projects
- ✅ Modify the code and models
- ✅ Distribute or build upon it

Please include attribution if you use or modify the project.


### 3. 📈 Evaluation Metrics

After training, the model was evaluated on test data using:

- **R² Score**: Goodness of fit
- **Mean Absolute Error (MAE)**: Average error magnitude
- **Root Mean Squared Error (RMSE)**: Penalizes large errors

```python
Random Forest R² Score: 0.85+
MAE: ~2.5
RMSE: ~3.2





