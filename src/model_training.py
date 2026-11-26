import pandas as pd
import joblib

# Model evaluation metrics
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_excel("data/crop_data.xlsx")

# Separate input features and target variable
X = df.drop("low_yield_risk", axis=1)
y = df["low_yield_risk"]

# Encode categorical variables
X = pd.get_dummies(
    X,
    columns=["region", "soil_type", "crop", "weather_condition"],
    dtype=int
)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

print("AGRI PAK - MODEL TRAINING")
print("=" * 40)
print("Random Forest model trained successfully!")
print("Training records:", len(X_train))
print("Testing records:", len(X_test))

# Make predictions
y_pred = model.predict(X_test)

# Calculate model accuracy
accuracy = accuracy_score(y_test, y_pred)

# Display evaluation results
print("\nMODEL EVALUATION")
print("=" * 40)

print("\nAccuracy:", accuracy * 100, "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Save the trained model
joblib.dump(model, "agri_pak_model.pkl")

print("\nModel saved successfully!")