import numpy as np
import pandas as pd
import seaborn as sns

df = sns.load_dataset("penguins")
# print(df.head())
# print(df.describe())

# print(df[df['bill_length_mm'] < 35])
# print(df.loc[df['bill_length_mm'] < 35])
# print(df.query('bill_length_mm < 35'))

# print(df.query('bill_length_mm > 55 and species == "Chinstrap"'))
# blmm = float(input("부리 길이 입력 : "))
# spcs = input("펭귄 종류(Gentoo / Chinstrap / Adelie  입력 : ")
# print(df.query('bill_length_mm >= @blmm and species == @spcs'))

# print(df.query('island.str.contains("sc")'))
# print(df.query('species.str.startswith("C")'))

penguins = ["Gentoo", "Chinstrap"]
print(df.query('species.isin(@penguins)'))