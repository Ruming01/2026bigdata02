import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = pd.read_csv('EV_charge.csv')

weekday_order = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

fig, ax = plt.subplots()
sns.boxplot(x='weekday', y='kwhTotal', data=df, ax=ax, order=weekday_order, hue='platform')
plt.show()

# fig = px.box(
#     data_frame=df, x='weekday', y='kwhTotal',
#     width=500, height=400,
#     category_orders={'weekday': ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']}, color='platform'
# )
# fig.show()
