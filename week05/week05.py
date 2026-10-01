import numpy as np
import pandas as pd
import seaborn as sns

df = sns.load_dataset('titanic')

def get_IQR(data):
    _3rd = data.quantile(.75)
    _1st = data.quantile(.25)
    return (np.abs(_3rd - _1st) * 1.5)

print(df.groupby(['sex','class'])['age'].apply(get_IQR))