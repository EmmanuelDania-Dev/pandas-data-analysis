import pandas as pd

df = pd.read_csv("data/raw/employees_messy.csv")

print(df)
print(df.isnull())
print(df.isnull().sum())
print(df.duplicated())
print(df.duplicated().sum())