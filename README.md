# Task 1: Data Cleaning and Preprocessing

## Objective

Clean and preprocess the Sales dataset using Python and Pandas.

## Summary of Changes

* Loaded and inspected the raw Sales dataset containing **8,399 rows and 21 columns**.
* Identified **63 missing values** in `Product Base Margin` and replaced them with the median value **0.52**.
* Checked for duplicate records; **no duplicates were found**.
* Standardized column names by converting them to lowercase and replacing spaces with underscores.
* Removed leading and trailing spaces from text values.
* Converted `Order Date` and `Ship Date` to datetime format.
* Checked and corrected numerical data types.
* Performed an IQR-based outlier check and identified **1,042 potential Sales outliers**.
* Final dataset contains **0 missing values and 0 duplicate records**.

## Tools Used

**Python, Pandas**

## Files

* `dataset/sales.csv` – Original dataset
* `output/cleaned_sales.csv` – Cleaned dataset
* `cleaning.py` – Data cleaning code
* `screenshots/` – Screenshots of the cleaning process
