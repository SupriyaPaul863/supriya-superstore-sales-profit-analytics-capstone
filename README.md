# 📊 Superstore Sales & Profit Analytics

## Problem Statement
Build a machine learning solution to predict the profit of a retail order before approving discounts, helping businesses maximize profitability while minimizing loss-making sales.

---

# 📁 Dataset

**Dataset Name:** Sample Superstore Dataset

**Source:** https://www.kaggle.com/datasets/vivek468/superstore-dataset-final

**Dataset Size**

- Records: 9,994
- Features: 21
- Target Variable: Profit

---

# 🛠 Tools & Libraries Used

### Programming & Analysis
- Python
- Jupyter Notebook
- SQL

### Data Processing
- Pandas
- NumPy

### Visualization
- Matplotlib
- Seaborn

### Machine Learning
- Scikit-learn
- Joblib

### Deployment
- Streamlit
- GitHub

---

# 🗄 SQL Questions Answered

The project answers the following business questions using SQL:

1. Total sales, profit and quantity sold
2. Top 10 highest-selling products
3. Top 10 most profitable products
4. Least profitable products
5. Sales and profit by category
6. Sales and profit by sub-category
7. Regional sales and profit analysis
8. Monthly sales trend
9. Yearly sales trend
10. Average discount by category
11. Products receiving the highest discounts
12. Customers generating the highest sales
13. Orders with negative profit
14. State-wise sales and profit analysis
15. Ship mode performance analysis

---

# 📈 Exploratory Data Analysis (EDA)

Key findings from the analysis include:

- Higher discounts generally lead to lower profits, with many high-discount orders resulting in losses.
- Technology products generate the highest profits, while Furniture contains a large proportion of loss-making orders.
- The profit distribution is highly skewed with several extreme outliers, making prediction more challenging.

---

# ⚙ Feature Engineering

The following features were created to improve model performance:

- DiscountAmount = Sales × Discount
- NetSales = Sales × (1 − Discount)
- LogSales (log transformation of Sales)
- HighDiscount (Binary feature indicating discount ≥30%)
- One-Hot Encoding for:
  - Category
  - Region
- Numerical feature scaling for Linear Regression

---

# 🤖 Models Used

| Model | Training R² | Testing R² | Remarks |
|--------|------------:|-----------:|---------|
| Linear Regression | ~0.49 | Negative | Underfitting |
| Decision Tree Regressor | ~1.00 | Negative | Severe overfitting |
| Random Forest Regressor | ~0.79 | ~0.06 | Best generalization |

---

# 🏆 Final Model Selected

**Random Forest Regressor**

### Why?

- Highest test performance among all models
- Lower overfitting than Decision Tree
- Captures nonlinear relationships
- More robust to outliers
- Produces the most reliable profit predictions

---

# 💼 Business Insights & Recommendations

- Avoid offering discounts above 30% unless strategically justified.
- Technology products consistently generate better profits and should receive higher inventory priority.
- Furniture products require optimized pricing and discount strategies.
- Use predictive analytics before approving discounts to identify potentially loss-making orders.
- Incorporate profit prediction into the sales workflow to support data-driven pricing decisions.

---

# 🚀 How to Run the Project

## 1. Clone the repository

```bash
git clone https://github.com/<your-username>/supriya-superstore-sales-profit-analytics-capstone.git
```

---

## 2. Navigate to the project

```bash
cd supriya-superstore-sales-profit-analytics-capstone
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run the Streamlit application

```bash
streamlit run app/app.py
```

---

## 5. Open in browser

```
http://localhost:8501
```

---

# 🎥 Demo Video

**Demo Video Link:**

_Add your YouTube or Google Drive video link here._

---

# 📂 Project Structure

```
├── app/
│   ├── app.py
│   └── requirements.txt
│
├── data/
│   ├── raw
│   └── processed
│
├── models/
│   └── best_profit_model.joblib
│
├── notebooks/
│   ├── EDA.ipynb
│   ├── Model_Training.ipynb
│   └── SQL_Analysis.ipynb
│
├── presentation/
│
├── README.md
│
└── requirements.txt
```

---

# 👩‍💻 Team Member

**Supriya Paul**

---

# ⭐ Future Improvements

- Hyperparameter optimization using Optuna or Bayesian Optimization
- XGBoost and LightGBM implementation
- Explainability using SHAP values
- Model monitoring and retraining pipeline
- Cloud deployment using Docker and Azure/AWS
- Interactive Power BI dashboard integration

---

## 📌 Project Outcome

This project demonstrates an end-to-end data science workflow—from SQL analysis and exploratory data analysis to feature engineering, machine learning model development, and deployment as an interactive Streamlit application—providing a practical decision-support tool for retail discount optimization.
