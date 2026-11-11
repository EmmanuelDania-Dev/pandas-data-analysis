
import pandas as pd


def check_required_columns(data, required_columns):
    missing_columns = [
        column for column in required_columns
        if column not in data.columns
    ]

    if missing_columns:
        print("Missing columns:", missing_columns)
        return False

    print("All required columns exist.")
    return True


def check_missing_values(data):
    missing = data.isnull().sum()

    print("\nMissing Values:")
    print(missing)

    total_missing = missing.sum()
    print("Total missing values:", total_missing)

    return total_missing == 0


def check_duplicates(data):
    duplicates = data.duplicated().sum()

    print("\nDuplicate records:", duplicates)

    return duplicates == 0


def check_invalid_values(data):
    negative_ages = (data["age"] < 0).sum()
    negative_salaries = (data["salary"] < 0).sum()

    empty_names = (
        data["employee_name"]
        .fillna("")
        .astype(str)
        .str.strip()
        .eq("")
        .sum()
    )

    print("\nInvalid Data:")
    print("Negative ages:", negative_ages)
    print("Negative salaries:", negative_salaries)
    print("Empty employee names:", empty_names)

    return (
        negative_ages == 0
        and negative_salaries == 0
        and empty_names == 0
    )


def check_data_types(data):
    checks = {
        "age": pd.api.types.is_integer_dtype(data["age"]),
        "salary": pd.api.types.is_numeric_dtype(data["salary"]),
        "employee_name": pd.api.types.is_string_dtype(
            data["employee_name"]
        ),
        "department": pd.api.types.is_string_dtype(
            data["department"]
        )
    }

    print("\nData Type Checks:")

    for column, valid in checks.items():
        print(f"{column}: {'Passed' if valid else 'Failed'}")

    return all(checks.values())


def validate_dataset(data):
    required_columns = [
        "employee_name",
        "age",
        "department",
        "salary"
    ]

    if not check_required_columns(data, required_columns):
        return False

    results = [
        check_missing_values(data),
        check_duplicates(data),
        check_invalid_values(data),
        check_data_types(data)
    ]

    return all(results)


if __name__ == "__main__":

    df = pd.read_csv(
        "data/processed/employees_cleaned.csv"
    )

    print("Dataset loaded successfully!")

    if validate_dataset(df):
        print("\nAll data validation checks passed!")
    else:
        print("\nData validation failed. Review the dataset.")
