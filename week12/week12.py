import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px

df = pd.read_csv('global_internet_users.csv')
df2 = sns.load_dataset('tips')


entities = ['South Korea', 'United Kingdom', 'Finland', 'United States']
df = df.loc[df['Entity'].isin(entities)]


# fig = px.scatter(
#     data_frame=df, x='Year', y='No. of Internet Users',
#     symbol = 'Entity', symbol_sequence=['cross','star','circle', 'square'],
#     size = 'No. of Internet Users',
#     width=400, height=400,
#     color='Entity', color_discrete_sequence=px.colors.qualitative.Safe
# )
# fig.show()

fig = px.scatter(
    data_frame=df2, x='total_bill', y='tip',
    color='smoker', size='size', symbol='time',
    width=600, height=400, color_discrete_sequence=px.colors.qualitative.Vivid
)
fig.show()