import pandas as pd
import numpy as np
import os

hungarian_path = os.path.join(os.getcwd(), 'Data', 'raw', 'hungarian.data')
switzerland_path = os.path.join(os.getcwd(), 'Data', 'raw', 'switzerland.data')
va_path = os.path.join(os.getcwd(), 'Data', 'raw', 'long-beach-va.data')
#new_path = os.path.join(os.getcwd(), 'Data', 'raw', 'new.data')



def get_patients(path):
    patients = []

    with open(path) as f:
        lines = [line.strip() for line in f]

    current_values = []

    for line in lines:
        parts = line.split()

        if not parts:
            continue

        if "name" in parts:

            current_values.extend(parts)

            patients.append(current_values)

            current_values = []

        else:
            current_values.extend(parts)
    return patients

column_names = [
"id", "ccf", "age", "sex", "painloc", "painexer", "relrest", "pncaden", "cp",
"trestbps", "htn", "chol", "smoke", "cigs", "years", "fbs", "dm", "famhist", 
"restecg", "ekgmo", "ekgday", "ekgyr", "dig", "prop", "nitr", "pro", "diuretic",
"proto", "thaldur", "thaltime", "met", "thalach", "thalrest", "tpeakbps", 
"tpeakbpd", "dummy", "trestbpd", "exang", "xhypo", "oldpeak", "slope", "rldv5",
"rldv5e", "ca", "restckm", "exerckm", "restef", "restwm", "exeref", "exerwm",
"thal", "thalsev", "thalpul", "earlobe", "cmo", "cday", "cyr", "num", "lmt",
"ladprox", "laddist", "diag", "cxmain", "ramus", "om1", "om2", "rcaprox", 
"rcadist", "lvx1", "lvx2", "lvx3", "lvx4", "lvf", "cathef", "junk", "name"
]
hungarian_patients = get_patients(hungarian_path)
va_patients = get_patients(va_path)
switzerland_patients = get_patients(switzerland_path)

hungarian_df = pd.DataFrame(hungarian_patients, columns=column_names)
va_df = pd.DataFrame(va_patients, columns=column_names)
switzerland_df = pd.DataFrame(switzerland_patients, columns=column_names)

df = pd.concat([hungarian_df, va_df, switzerland_df])

df.replace("?", np.nan, inplace=True)
df.replace("NA", np.nan, inplace=True)
df.replace("-9", np.nan, inplace=True)

df = df.apply(pd.to_numeric, errors="ignore")

relevant_columns = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach",
    "exang", "oldpeak", "slope", "ca", "thal", "num"
]

df= df[relevant_columns]

df = df.drop_duplicates()

df.to_csv("Data/processed/clean_heart_disease.data", index=False)