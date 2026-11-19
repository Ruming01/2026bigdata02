import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px

df = pd.read_csv('global_internet_users.csv')

entities = ['South Korea', 'United Kingdom', 'Finland', 'North Korea', 'China', 'India', 'Italy', 'Japan', 'Spain']
df = df.loc[df['Entity'].isin(entities)]

# c = px.colors.qualitative.Light24
c = px.colors.qualitative.Safe
fig = px.scatter(
    data_frame=df, x='Year', y='No. of Internet Users',
    width=400, height=400,
    color='Entity', color_discrete_sequence=c
)
fig.show()