import pandas as pd

df = pd.read_csv("data/processed/employees_cleaned.csv")

print(df.sort_values(by="age"))
print(df.sort_values(by="salary", ascending=False))
print(df.sort_values(by="employee_name"))
print(
    df.sort_values(
        by=["department", "salary"],
        ascending=[True, False]
    )
)