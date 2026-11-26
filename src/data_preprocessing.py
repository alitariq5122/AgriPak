#import pandas as pd
# Load the agricultural dataset
#df = pd.read_excel("data/crop_data.xlsx")

# Separate input features (X) and target variable (y)
#X = df.drop("low_yield_risk", axis=1)
#y = df["low_yield_risk"]

# Display results
#print("AGRI PAK - DATA PREPROCESSING")
#print("=" * 40)

#print("\nInput Features (X):")
#print(X.head())

#print("\nTarget Variable (y):")
#print(y.head())

#print("\nFeature Shape:", X.shape)
#print("Target Shape:", y.shape)

import pandas as pd

# Load the agricultural dataset
df = pd.read_excel("data/crop_data.xlsx")

# Separate input features (X) and target variable (y)
X = df.drop("low_yield_risk", axis=1)
y = df["low_yield_risk"]

# Convert categorical variables into numerical values
X = pd.get_dummies(
    X,
    columns=["region", "soil_type", "crop", "weather_condition"],
    dtype=int
)

# Display results
print("AGRI PAK - CATEGORICAL ENCODING")
print("=" * 40)

print("\nEncoded Features:")
print(X.head())

print("\nEncoded Feature Columns:")
print(X.columns.tolist())

print("\nNew Feature Shape:", X.shape)

from sklearn.model_selection import train_test_split

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Display results
print("\nAGRI PAK - TRAIN TEST SPLIT")
print("=" * 40)

print("\nTraining Features:", X_train.shape)
print("Testing Features:", X_test.shape)

print("\nTraining Target:", y_train.shape)
print("Testing Target:", y_test.shape)