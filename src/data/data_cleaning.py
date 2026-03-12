import pandas as pd
import numpy as np
import os

hungarian_path = os.path.join(os.getcwd(), '..','..', 'Data', 'raw', 'hungarian.data')
switzerland_path = os.path.join(os.getcwd(), '..','..', 'Data', 'raw', 'switzerland.data')
va_path = os.path.join(os.getcwd(), '..','..', 'Data', 'raw', 'long-beach.va.data')
new_path = os.path.join(os.getcwd(), '..', '..', 'Data', 'raw', 'new.data')


hungarian_df = pd.read_csv(hungarian_path, header=None)
switzerland_df = pd.read_csv(switzerland_path, header=None)
va_df = pd.read_csv(va_path, header=None)
new_df = pd.read_csv(va_path, header=None)