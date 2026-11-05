import pandas as pd

df = pd.read_csv('product_inspection.csv')
df['date'] = pd.to_datetime(df['date'])
# print(df.head())
# print(df.info())
# print(df['inspection_step'].value_counts())

print(df[df['date'] == '2022-01-01'])