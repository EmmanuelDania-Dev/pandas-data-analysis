import pandas as pd

employees = pd.read_csv("data/raw/employee.csv")
salaries = pd.read_csv("data/raw/salaries.csv")

merged_df = pd.merge(
    employees,
    salaries,
    on="employee_id",
    how="outer"
)

print(merged_df)