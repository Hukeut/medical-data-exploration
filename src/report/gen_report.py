import pandas as pd
import pandas as pd

import seaborn as sns
from ydata_profiling import ProfileReport
import os



clean_heart_disease_data_path = os.path.join(os.getcwd(), 'Data', 'processed', 'clean_heart_disease.data')
df = pd.read_csv(clean_heart_disease_data_path, header=None)

profile = ProfileReport(df)

eda_report_path = os.path.join(os.getcwd(), 'reports', 'eda_report.html')

profile = ProfileReport(
    df,
    title="Heart Disease Dataset — Exploratory Data Analysis",
    explorative=True
)

profile.to_file(eda_report_path )