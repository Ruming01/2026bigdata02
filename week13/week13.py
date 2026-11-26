import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
fig, ax = plt.subplots()
sns.histplot(df, x='total_bill', ax=ax, bins=8) # 계급구간 8
plt.show()