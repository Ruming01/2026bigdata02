import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df1 = pd.read_csv('weight_height.csv')

# print(df1.info())
# print(df1.head())
# print(df1.tail())
# print(df1['Gender'].value_counts())

df2 = df1.query('Weight < 300') # 이상치 제거
print(df1.describe())
print(df2.describe())

sns.scatterplot(x='Weight', y='Height', data=df1)
sns.scatterplot(x='Weight', y='Height', data=df2)
plt.show()