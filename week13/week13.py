import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

df = sns.load_dataset("tips")

# fig = px.histogram(data_frame=df, x='total_bill', width=450)
# fig = px.histogram(data_frame=df, x='total_bill', width=550, nbins=20)
fig = px.histogram(data_frame=df, x='total_bill', width=550, color='time', barmode='overlay')
fig.show()

