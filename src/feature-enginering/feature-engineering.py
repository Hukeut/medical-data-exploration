import pandas as pd
import os
from sklearn.preprocessing import StandardScaler



clean_heart_disease_data_path = os.path.join(os.getcwd(), 'Data', 'processed', 'clean_heart_disease.data')
df = pd.read_csv(clean_heart_disease_data_path, sep=',')
df.head()

target = "num"

numerical_features = [
    "age",
    "trestbps",
    "chol",
    "thalach",
    "oldpeak"
]

binary_features = [
    "sex",
    "fbs",
    "exang"
]

categorical_features = [
    "cp",
    "restecg",
    "slope",
    "thal",
    "ca"
]

df_encoded = pd.get_dummies(
    df,
    columns=categorical_features,
    drop_first=True
)


scaler = StandardScaler()

df_encoded = df_encoded.dropna()

df_encoded[numerical_features] = scaler.fit_transform(
    df_encoded[numerical_features]
)

X = df_encoded.drop("num", axis=1)
y = df_encoded["num"]

df_encoded.to_csv("Data/processed/df.data", index=False)
X.to_csv("Data/processed/X.data", index=False)
y.to_csv("Data/processed/y.data", index=False)