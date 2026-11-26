#import tells Python to load a library.
#pandas is a Python library used for working with data.
#as pd gives Pandas a short name (alias).
# Why do we need Pandas?
#Our dataset is an Excel file containing 50,000 agricultural records. Pandas helps us read, organize, analyze and manipulate this data.
import pandas as pd

# Load the agricultural dataset
# df is the Variable that stores our dataset
df = pd.read_excel("data/crop_data.xlsx")

# Display basic dataset information
print("AGRI PAK - DATA EXPLORATION")
print("=" * 40)

# df.shape returns the dimensions of our dataset.
#\n means start a new line.
print("\nDataset Shape:")
print(df.shape)

#df.columns retrieves all column names.
#.tolist() converts them into a Python list.
#print() displays that list.
print("\nColumn Names:")
print(df.columns.tolist())

#df.head() displays the first five rows of the dataset by default.
print("\nFirst 5 Records:")
print(df.head())

#df.info() provides:
# Total number of rows.
# Total number of columns.
# Column names.
# Number of non-null values.
# Data types.
# Memory usage.
print("\nDataset Information:")
df.info()

# df.isnull().sum() Checks for missing values and then count them
print("\nMissing Values:")
print(df.isnull().sum())

# df.duplicated().sum() Checks for duplicate records and count them
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Check low-yield risk distribution
print("\nLow-Yield Risk Distribution:")
print(df["low_yield_risk"].value_counts())

# Check percentage distribution
print("\nLow-Yield Risk Percentage:")
print(df["low_yield_risk"].value_counts(normalize=True) * 100)

# Statistical summary of numerical columns
print("\nStatistical Summary:")
# df.describe() calculates statistical information about numerical columns:
#Statistic	Meaning
#count	    Number of available values
#mean	    Average
#std	    Standard deviation
#min	    Minimum value
#25%	    First quartile
#50%	    Median
#75%	    Third quartile
#max	    Maximum value
print(df.describe())