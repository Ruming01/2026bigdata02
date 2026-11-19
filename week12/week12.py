import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px

df1 = sns.load_dataset('tips')

#review week7
# s: slope, i: intercept, r: correlation
# s, i, r, _, _ = linregress(df1['MILES*'], df1['DURATION*'])  # x축은 운행거리, y축은 운행시간
# print(s, i, r)  # 기울기, 절편, 상관계수(-1~1) 출력. 강한 양의 상관관계.

fig, ax = plt.subplots()
sns.regplot(x='total_bill', y='tip', data=df1, ax=ax)

plt.show()