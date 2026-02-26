# =====================================================
# TASK 1 – Data Immersion & Wrangling
# Dataset Type: Sales Transactions / Customer Data
# =====================================================

import pandas as pd
import numpy as np

print("========== TASK 1 STARTED ==========\n")

# -----------------------------------------------------
# STEP 1: CREATE SAMPLE RAW DATASET (With Issues)
# -----------------------------------------------------

raw_data = {
    "Customer_ID": ["C001", "C002", "C003", "C003", "C004", "C005"],
    "Customer_Name": ["Ramesh ", "Sita", "Arjun", "Arjun", "Priya", "Kiran"],
    "Date_of_Birth": ["1999-05-12", "1992/08/20", "1996-07-15", "1996-07-15", "1985-09-10", None],
    "Gender": ["Male", "F", "male", "male", "Female", "M"],
    "Product": ["Laptop", "Mobile", "Tablet", "Tablet", "Laptop", "Mobile"],
    "Purchase_Amount": [55000, 25000, 15000, 15000, 62000, None],
    "Purchase_Date": ["01-01-2024", "2024/01/05", "05-01-2024", "05-01-2024", "10-01-2024", "2024-01-12"]
}

df = pd.DataFrame(raw_data)

print("Raw Dataset:\n")
print(df)
print("\n-------------------------------------")

# Save raw dataset
df.to_csv("raw_sales_data.csv", index=False)

# -----------------------------------------------------
# STEP 2: DATA PROFILING (Identify Issues)
# -----------------------------------------------------

print("\nMissing Values:\n")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\n-------------------------------------")

# -----------------------------------------------------
# STEP 3: DATA CLEANING
# -----------------------------------------------------

# Remove duplicates
df = df.drop_duplicates()

# Trim extra spaces
df["Customer_Name"] = df["Customer_Name"].str.strip()

# Standardize Gender column
df["Gender"] = df["Gender"].replace({
    "male": "Male",
    "M": "Male",
    "F": "Female"
})

# Convert Purchase_Amount to numeric and fill missing with median
df["Purchase_Amount"] = pd.to_numeric(df["Purchase_Amount"], errors="coerce")
df["Purchase_Amount"] = df["Purchase_Amount"].fillna(df["Purchase_Amount"].median())

# Convert Date columns to proper datetime format
df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"], errors="coerce")
df["Date_of_Birth"] = pd.to_datetime(df["Date_of_Birth"], errors="coerce")

# Fill missing DOB with median year assumption
median_dob = df["Date_of_Birth"].median()
df["Date_of_Birth"] = df["Date_of_Birth"].fillna(median_dob)

# Feature Engineering: Create Age Column
current_year = 2024
df["Customer_Age"] = current_year - df["Date_of_Birth"].dt.year

# Create Age Group Column
df["Age_Group"] = df["Customer_Age"].apply(
    lambda x: "Young" if x < 30 else "Adult"
)

# Standardize Purchase_Date format
df["Purchase_Date"] = df["Purchase_Date"].dt.strftime("%Y-%m-%d")

# -----------------------------------------------------
# STEP 4: FINAL CLEANED DATASET
# -----------------------------------------------------

print("\nCleaned Dataset:\n")
print(df)

# Save cleaned dataset
df.to_csv("cleaned_sales_data.csv", index=False)

print("\n========== TASK 1 COMPLETED SUCCESSFULLY ==========")
print("Files Generated:")
print("1. raw_sales_data.csv")
print("2. cleaned_sales_data.csv")