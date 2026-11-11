import pandas as pd

df = pd.read_csv("data/processed/employees_cleaned.csv")

# Employees name
print(df["employee_name"])

# Employees department and salary
print(df[["department", "salary"]])

# Employees earning above 200000
print(df[df["salary"] > 200000])

# Employees aged 18 or above
print(df[df["age"] >= 18])

# Employees in Finance
print(df[df["department"] == "Finance"])

# Combining conditions using "&"
print(df[(df["department"] == "Engineering") & (df["salary"] > 200000)])

# Combining conditions using "|" meaning OR
print(df[(df["department"] == "Finance") | (df["department"] == "Engineering")])