import pandas as pd

df = pd.read_csv("data/raw/employees.csv")

print(df)
print(df.head(3))
print(df.tail())
print(df.columns)
print(df.dtypes)

df.info()