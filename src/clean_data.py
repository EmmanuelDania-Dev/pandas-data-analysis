import pandas as pd

df = pd.read_csv("data/raw/employees_messy.csv")

print("Original data:")
print(df)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate records:")
print(df.duplicated().sum())

df = df.drop_duplicates()

median_age = df["age"].median()

df["age"] = df["age"].fillna(median_age)

df["age"] = df["age"].astype(int)

print("\nCleaned data:")
print(df)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nDuplicates after cleaning:")
print(df.duplicated().sum())

print("\nData Quality Checks:")

print("Missing ages:", df["age"].isnull().sum())

print("Duplicate records:", df.duplicated().sum())

print("Invalid ages:", (df["age"] < 0).sum())

print("Age data type:", df["age"].dtype)

print("Missing salaries:", df["salary"].isnull().sum())

df.to_csv("data/processed/employees_cleaned.csv", index=False)