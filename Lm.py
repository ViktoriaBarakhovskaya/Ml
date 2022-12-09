import numpy as np
import pandas as pd
df = pd.read_csv('D:\\ML and Data Science\\UNZIP_ME_FOR_NOTEBOOKS_ML_RUS_V1\\03-Pandas\\tips.csv')
print(df.columns)
print(df['total_bill'].sum())
print(df['tip'].mean())


