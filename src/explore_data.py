import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/processed/employees_cleaned.csv")

# Display dataset
print(df)

# Preview first 5 rows
print(df.head())

# Dataset dimensions
print("Dataset shape:", df.shape)

# Column names
print("Columns:", df.columns)

# Data types
print(df.dtypes)

# Dataset information
df.info()

# Statistical summary
print(df.describe())

# Number of employees per department
print(df["department"].value_counts())

# Average salary per department
print(df.groupby("department")["salary"].mean())

# Department analysis
department_summary = df.groupby("department")["salary"].agg(
    ["mean", "sum", "min", "max", "count"]
)

print("\nDepartment Salary Summary:")
print(department_summary)

# Export department analysis
department_summary.to_csv(
    "data/processed/department_summary.csv"
)

print("\nDepartment summary exported successfully.")