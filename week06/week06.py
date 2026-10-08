import seaborn as sns
import pandas as pd
import numpy as np

df = pd.read_csv('APPL_price.csv')
# print(df.head())
# print(df.tail())
# print(df.info())
df['Date'] = pd.to_datetime(df['Date'])
# print(df.info())
df = df.set_index('Date')
# print(df.head())

# print(df['1990-11-02':'1990-11-10'])
print(df['2021-04':'2021-04'])