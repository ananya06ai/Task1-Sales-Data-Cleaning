import pandas as pd
import os

# ============================================
# TASK 1: DATA CLEANING AND PREPROCESSING
# ============================================

# 1. LOAD RAW DATASET
# ============================================

file_path = "dataset/sales.csv"

df = pd.read_csv(file_path, encoding="latin1")

print("\n========================================")
print("       RAW DATASET INFORMATION")
print("========================================")

print("Number of rows and columns:", df.shape)

# ============================================
# 2. CHECK MISSING VALUES
# ============================================

print("\n--- Missing Values Before Cleaning ---")
missing_before = df.isnull().sum()
print(missing_before)

print("\nTotal missing values:",
      df.isnull().sum().sum())

# ============================================
# 3. CHECK DUPLICATE RECORDS
# ============================================

print("\n--- Duplicate Records Before Cleaning ---")
duplicates_before = df.duplicated().sum()

print("Duplicate rows:", duplicates_before)

# ============================================
# 4. STANDARDIZE COLUMN NAMES
# ============================================

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\n--- Standardized Column Names ---")
print(df.columns.tolist())

# ============================================
# 5. REMOVE DUPLICATE RECORDS
# ============================================

df = df.drop_duplicates()

# ============================================
# 6. HANDLE MISSING VALUES
# ============================================

# Product Base Margin contains missing values.
# Replace missing values with the median.

if "product_base_margin" in df.columns:

    median_value = df["product_base_margin"].median()

    df["product_base_margin"] = (
        df["product_base_margin"].fillna(median_value)
    )

    print("\nProduct Base Margin missing values")
    print("replaced using median:", median_value)

# ============================================
# 7. STANDARDIZE TEXT VALUES
# ============================================

text_columns = df.select_dtypes(include="object").columns

for column in text_columns:
    df[column] = df[column].str.strip()

print("\nText values standardized by removing")
print("leading and trailing spaces.")

# ============================================
# 8. CONVERT DATE COLUMNS
# ============================================

if "order_date" in df.columns:

    df["order_date"] = pd.to_datetime(
        df["order_date"],
        errors="coerce"
    )

if "ship_date" in df.columns:

    df["ship_date"] = pd.to_datetime(
        df["ship_date"],
        errors="coerce"
    )

print("\nDate columns converted to datetime.")

# ============================================
# 9. CHECK AND FIX DATA TYPES
# ============================================

# Integer columns

integer_columns = [
    "row_id",
    "order_id",
    "order_quantity"
]

for column in integer_columns:

    if column in df.columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

# Numerical columns

numeric_columns = [
    "sales",
    "discount",
    "profit",
    "unit_price",
    "shipping_cost",
    "product_base_margin"
]

for column in numeric_columns:

    if column in df.columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

print("\nNumeric data types checked and converted.")

# ============================================
# 10. CHECK FOR INVALID / MISSING DATES
# ============================================

print("\n--- Missing Dates After Conversion ---")

if "order_date" in df.columns:
    print(
        "Order Date missing:",
        df["order_date"].isnull().sum()
    )

if "ship_date" in df.columns:
    print(
        "Ship Date missing:",
        df["ship_date"].isnull().sum()
    )

# ============================================
# 11. OUTLIER CHECK
# ============================================

print("\n--- Outlier Check ---")

if "sales" in df.columns:

    Q1 = df["sales"].quantile(0.25)
    Q3 = df["sales"].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[
        (df["sales"] < lower_limit) |
        (df["sales"] > upper_limit)
    ]

    print("Sales outliers detected:", len(outliers))

# ============================================
# 12. FINAL DATA QUALITY CHECK
# ============================================

print("\n========================================")
print("       FINAL DATA QUALITY CHECK")
print("========================================")

print("\nFinal dataset shape:")
print(df.shape)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nTotal missing values after cleaning:")
print(df.isnull().sum().sum())

print("\nDuplicate rows after cleaning:")
print(df.duplicated().sum())

print("\nFinal data types:")
print(df.dtypes)

# ============================================
# 13. CREATE OUTPUT FOLDER
# ============================================

os.makedirs("output", exist_ok=True)

# ============================================
# 14. SAVE CLEANED DATASET
# ============================================

output_file = "output/cleaned_sales.csv"

df.to_csv(
    output_file,
    index=False
)

print("\n========================================")
print("       CLEANING COMPLETED")
print("========================================")

print("\nCleaned dataset saved successfully!")

print("File location:")
print(output_file)