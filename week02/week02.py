import numpy as np
import pandas as pd

df1 = pd.read_csv("bike.csv")
# print(df1.head(5))
# print(df1.info())
# print(df1['temp'])

# print(df1.iloc[3:8, 3:7])
# print(df1.loc[4:9, 'workingday':'atemp'])
print(df1.loc[df1['season'] != 1])