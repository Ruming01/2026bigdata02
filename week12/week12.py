import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress
import plotly.express as px
import statsmodels.api as sm

df1 = sns.load_dataset('tips')

fig = px.scatter(data_frame=df1, x='total_bill', y='tip', width=500, height=400, trendline='ols', color='smoker')
fig.show()