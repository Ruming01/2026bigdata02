import seaborn as sns
import pandas as pd
import numpy as np

df = pd.read_csv('APPL_price.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

# print(df['1990-11-02':'1990-11-10'])
# print(df['2021-04':'2021-04'])

print(df.resample('1ME').mean())