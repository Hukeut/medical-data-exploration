# Heart Disease Analysis Project

## Project Overview

This project demonstrates a **reproducible data analysis and machine learning workflow** using Python and Jupyter notebooks.  
The focus is on clean, clear results (“straight outputs”), well-documented notebooks, and a reproducible environment for anyone to run the project from scratch.

---

## Project Goals

1. **Data Handling**
   - Collect, clean, and preprocess the dataset.
   - Handle missing or inconsistent data entries.

2. **Exploratory Data Analysis (EDA)**
   - Visualize distributions, correlations, and trends.
   - Identify key patterns and insights in the data.

3. **Modeling & Evaluation**
   - Train and evaluate machine learning models.
   - Compare performance using standard metrics.

4. **Reproducibility**
   - Provide a virtual environment (`hdenv`) and `requirements.txt`.
   - Include an `init.sh` script to install all dependencies and register the environment with Jupyter.

5. **Documentation & Presentation**
   - Maintain clean notebooks with final outputs only.
   - Explain code, methodology, and results clearly.

---

## Dataset Information

> ⚠️ **Note:** The original Cleveland dataset referenced in similar projects is currently broken in the repository.  
> This project uses a replacement publicly available dataset suitable for the same type of analysis.

- **Dataset source:** [Alternative Heart Disease Dataset on Kaggle](https://www.kaggle.com/datasets/ronitf/heart-disease-uci)
- **Format:** CSV
- **Features:** Age, sex, chest pain type, resting blood pressure, cholesterol, fasting blood sugar, etc.
- **Target:** Presence of heart disease (1 = yes, 0 = no)

> You can download the dataset manually or include it in the `data/` folder.

---

## Project Structure

![CI](https://github.com/<your-username>/<repo>/actions/workflows/ci.yml/badge.svg)

project/
│
├── src/                  # All Python modules
│   ├── data/             # Data loading & preprocessing
│   ├── features/         # Feature engineering
│   ├── models/           # ML models & training
│   └── visualization/    # Plotting & dashboards
├── notebooks/            # Minimal notebooks for demonstration
├── tests/                # Unit tests
├── data/                 # CSV or raw data
├── requirements.txt
├── init.sh
├── .gitignore # Ignore virtual env and checkpoints
├── hdenv/ # Python virtual environment (ignored by git)
└── README.md


---

## Setup Instructions

1. **Clone the repository:**

```bash
git clone <https://github.com/Hukeut/medical-data-exploration.git>
cd <medical-data-exploration>

./init.sh

source hdenv/bin/activate


## Exploratory Data Analysis

An automated exploratory data analysis report was generated using ydata-profiling.

You can view the full report here:
reports/eda_report.html

# Conclusion

This project explored the UCI Heart Disease dataset with the goal of predicting the presence of heart disease using machine learning techniques.

After performing data cleaning, feature selection, and exploratory data analysis, a baseline Logistic Regression model was implemented, achieving approximately 80% accuracy. The problem was carefully reformulated as a binary classification task to align with clinical decision-making.

Further improvements were achieved using ensemble methods such as Random Forest and Gradient Boosting, combined with hyperparameter tuning and cross-validation. These approaches increased performance to the 79–83% range while maintaining generalization.

Special attention was given to avoiding data leakage, handling missing values, and selecting clinically relevant features. Evaluation metrics such as precision, recall, and F1-score were analyzed, with a focus on maximizing recall for the positive class (heart disease), which is critical in a medical context.

Overall, this project demonstrates the importance of proper data preprocessing, model selection, and evaluation in building reliable predictive models in healthcare applications.

# Future Work 

Future improvements could include:

Using larger and more diverse medical datasets
Applying advanced models such as XGBoost or deep learning
Incorporating domain knowledge for feature engineering
Optimizing decision thresholds based on clinical risk tolerance