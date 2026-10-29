import pandas as pd


df = pd.read_csv('us_confirmed.csv')
df['Date'] = pd.to_datetime(df['Date'])
# print(df.info())

# head
# print(df.head())

# datetime index를 가진 테이블의 시간 슬라이싱
df = df.set_index('Date').sort_values('Date')
# print(df['2021-01':'2020-06'])

# 문자열 index를 가진 데이터테이블
df = df.reset_index().set_index('Province/State').sort_index()
# print(df.index.unique())
# states = list(df.index.unique())
# print(len(states)) # 미국 주, 연방구역, 자치령, 특수 목적의 배 포함

print(df['Ca':'cp']) #california to connecticut