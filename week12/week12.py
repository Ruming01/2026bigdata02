import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px
import numpy as np

df1 = sns.load_dataset('tips')


x = np.arange(-2, 10, 1)
y = x**3 - 9*x**2 + x + 4
# y = 9*x**2 + x + 4

fig, ax = plt.subplots()
# sns.regplot(x=x, y=y, ax=ax, order=3)

sns.regplot(
    x=x, y=y, ax=ax, order=3,
    scatter_kws={'s':50}, line_kws={'color':'blue', 'linestyle':'--'}
)


plt.show()