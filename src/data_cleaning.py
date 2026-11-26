
import pandas as pd

# Load the original CSV dataset
df = pd.read_csv("data/crop_data.csv")

print("AGRIPAK - DATA CLEANING")
print("=" * 40)

# Display original dataset information
print("\nOriginal Dataset Shape:", df.shape)

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

print("\nDuplicate Records Before Cleaning:")
print(df.duplicated().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Define numerical and categorical columns
numerical_columns = [
    "rainfall_mm",
    "temperature_c",
    "fertilizer_used",
    "irrigation_used",
    "days_to_harvest",
    "low_yield_risk"
]

categorical_columns = [
    "region",
    "soil_type",
    "crop",
    "weather_condition"
]

# Convert numerical columns to numeric data types
for column in numerical_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Remove records with missing target values
df = df.dropna(subset=["low_yield_risk"])

# Fill missing numerical feature values with their median
for column in numerical_columns:
    if column != "low_yield_risk":
        df[column] = df[column].fillna(df[column].median())

# Convert categorical columns to string
for column in categorical_columns:
    df[column] = df[column].astype("string")

    # Fill missing categorical values with the most frequent value
    if df[column].isnull().any():
        df[column] = df[column].fillna(df[column].mode()[0])

# Convert binary and target columns to integers
for column in ["fertilizer_used", "irrigation_used", "low_yield_risk"]:
    df[column] = df[column].astype(int)

# Save cleaned dataset
df.to_csv("data/crop_data_cleaned.csv", index=False)

# Display final results
print("\nCLEANING RESULTS")
print("=" * 40)

print("\nCleaned Dataset Shape:", df.shape)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDuplicate Records After Cleaning:")
print(df.duplicated().sum())

print("\nFinal Data Types:")
print(df.dtypes)

print("\nCleaned dataset saved successfully!")
