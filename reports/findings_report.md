# Employee Data Analysis Report

## 1. Introduction

This project analyses an employee dataset using Python and Pandas. The objective was to clean the dataset, validate its quality, explore employee information and identify salary patterns across departments.

## 2. Dataset Overview

The cleaned dataset contains:
- 7 employee records.
- 4 columns: employee_name, age, department and salary.
- 5 departments.

## 3. Data Cleaning

The following cleaning operations were performed:
- Removed duplicate records.
- Identified missing values.
- Replaced missing ages using the median age.
- Converted the age column to integers.
- Exported the cleaned dataset.

## 4. Data Quality Validation

Automated checks were implemented to verify:
- Required columns.
- Missing values.
- Duplicate records.
- Invalid ages and salaries.
- Empty employee names.
- Expected data types.

All validation checks passed on the final cleaned dataset.

## 5. Key Findings

- The average employee age is approximately 17.86 years.
- The average recorded salary is approximately 235,714.29.
- Engineering has the highest departmental average salary at 325,000.
- Information Tech has the lowest departmental average salary at 180,000.
- Engineering and Finance have the highest employee counts, with two employees each.

## 6. Conclusion

The project demonstrates how Pandas can be used to clean, validate, explore, merge and analyse tabular datasets.

The analysis produced a cleaned employee dataset and departmental salary summary. Automated validation functions were also developed to improve data reliability and make the analysis process reusable.

## 7. Tools and Technologies

- Python
- Pandas
- CSV
- Git and GitHub