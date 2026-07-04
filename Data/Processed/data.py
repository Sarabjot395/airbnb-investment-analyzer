import pandas as pd
df=pd.read_csv("Data/Raw/AB_US_2020.csv")
print(df.head(5))
print(df.info())
print(df['city'].nunique())
print(df['city'].unique())