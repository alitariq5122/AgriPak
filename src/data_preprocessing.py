
import pandas as pd
import os

from sklearn.model_selection import train_test_split

# Load cleaned agricultural dataset
df = pd.read_csv("data/crop_data_cleaned.csv")

# Separate input features and target variable
X = df.drop("low_yield_risk", axis=1)
y = df["low_yield_risk"]

# Convert categorical variables into numerical values
X = pd.get_dummies(
    X,
    columns=["region", "soil_type", "crop", "weather_condition"],
    dtype=int
)

# Display encoded features
print("AGRI PAK - CATEGORICAL ENCODING")
print("=" * 40)

print("\nEncoded Features:")
print(X.head())

print("\nEncoded Feature Columns:")
print(X.columns.tolist())

print("\nNew Feature Shape:", X.shape)

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create folder for split files
os.makedirs("data/splits", exist_ok=True)

# Save training and testing datasets
X_train.to_csv("data/splits/X_train.csv", index=False)
X_test.to_csv("data/splits/X_test.csv", index=False)

y_train.to_csv("data/splits/y_train.csv", index=False)
y_test.to_csv("data/splits/y_test.csv", index=False)

# Display split results
print("\nAGRI PAK - TRAIN TEST SPLIT")
print("=" * 40)

print("\nTraining Features:", X_train.shape)
print("Testing Features:", X_test.shape)

print("\nTraining Target:", y_train.shape)
print("Testing Target:", y_test.shape)

print("\nTraining and testing files saved successfully!")