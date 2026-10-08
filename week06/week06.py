import seaborn as sns
import pandas as pd
import numpy as np

df = sns.load_dataset("titanic")
# print(df.head())
# print(df.groupby('sex')['survived'].mean())
# print(df.groupby(['sex','class'])['survived'].mean())
# print(df.groupby(['sex','class'])['survived'].agg(['mean','count', 'median']))
print(df.groupby(['sex','class'])[['survived','age']].agg({'survived':'mean', 'age':'min'}))

def get_IQR(data):
    _3rd = data.quantile(.75)
    _1st = data.quantile(.25)
    return (np.abs(_3rd - _1st) * 1.5)

print(df.groupby(['sex','class'])['age'].apply(get_IQR))