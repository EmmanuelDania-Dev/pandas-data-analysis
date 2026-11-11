# Week 7 Internship Project: Employee Data Analysis with Python and Pandas

## Project Overview

This project was developed as part of the **Week 7 FlexiSAF Internship Project**.

It demonstrates the use of Python and Pandas for data cleaning, data quality validation, data manipulation and exploratory data analysis.

The project uses employee datasets to demonstrate how raw data can be transformed into structured, reliable and meaningful information.

## Project Objectives

- Load and inspect tabular datasets.
- Identify and handle missing values.
- Detect and remove duplicate records.
- Convert columns to appropriate data types.
- Filter and sort records.
- Merge multiple datasets.
- Group and aggregate data.
- Perform automated data quality validation.
- Export cleaned datasets and analysis results.

## Technologies Used

- Python
- Pandas
- CSV
- Git
- GitHub

## Project Structure

```text
pandas-data-analysis/
├── data/
│   ├── raw/
│   └── processed/
├── reports/
│   └── findings_report.md
├── scripts/
│   ├── data_grouping.py
│   ├── data_merging.py
│   ├── data_sorting.py
│   └── data_validation.py
├── src/
│   ├── check_quality.py
│   ├── clean_data.py
│   ├── explore_data.py
│   ├── filter_data.py
│   └── load_data.py
├── tests/
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/EmmanuelDania-Dev/pandas-data-analysis.git
```

Navigate into the project directory:

```bash
cd pandas-data-analysis
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project

Run commands from the project root directory.

Clean the dataset:

```bash
python src/clean_data.py
```

Explore the dataset:

```bash
python src/explore_data.py
```

Run data validation:

```bash
python scripts/data_validation.py
```

Other scripts demonstrate data loading, filtering, sorting, grouping, merging and quality checks.

## Project Outputs

The project generates:

- `employees_cleaned.csv`: Cleaned employee dataset.
- `department_summary.csv`: Department-level salary statistics.
- `findings_report.md`: Summary of the analysis and key findings.

## Key Findings

Based on the cleaned employee dataset:

- Total employee records: 7.
- Number of departments: 5.
- Average employee age: approximately 17.86.
- Overall average recorded salary: approximately 235,714.29.
- Engineering has the highest average recorded salary at 325,000.
- Information Tech has the lowest average recorded salary at 180,000.

These findings describe the sample dataset and should not be interpreted as general employment statistics.

## Demo Recording

This is a recording of the project running successfully:
https://drive.google.com/file/d/1esPfoe49GNOnwVj0R0Gvjao5n_ccO9vO/view?usp=sharing

## Author

**Emmanuel Dania**

GitHub: https://github.com/EmmanuelDania-Dev

## Internship

**Project:** Week 7 FlexiSAF Internship Project  
**Focus:** Data Analysis with Python and Pandas