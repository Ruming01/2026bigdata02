import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

df1 = sns.load_dataset('tips')


# s: slope, i: intercept, r: correlation
s, i, r, _, _ = linregress(df1['total_bill'], df1['tip'])  # x축은 운행거리, y축은 운행시간
# print(s, i, r)  # 기울기, 절편, 상관계수(-1~1) 출력. 강한 양의 상관관계.

fig, ax = plt.subplots()
sns.regplot(x='total_bill', y='tip', data=df1, ax=ax, ci=None, line_kws={'label': f'y={s:.2f}x+{i:.2f}, R^2={r**2:.2f}'})
plt.legend()
plt.show()