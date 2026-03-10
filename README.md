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

