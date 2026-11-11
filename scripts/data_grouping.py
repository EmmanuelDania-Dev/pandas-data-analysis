import pandas as pd

df = pd.read_csv("data/processed/employees_cleaned.csv")

print(df.groupby("department")["salary"].mean())
print(df.groupby("department")["salary"].sum())
print(df.groupby("department")["salary"].max())
print(df.groupby("department")["employee_name"].count())
summary = df.groupby("department")["salary"].agg(
    ["mean", "sum", "min", "max", "count"]
)

print(summary)