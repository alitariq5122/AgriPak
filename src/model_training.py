
import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# Load the saved training and testing datasets
X_train = pd.read_csv("data/splits/X_train.csv")
X_test = pd.read_csv("data/splits/X_test.csv")
y_train = pd.read_csv("data/splits/y_train.csv").squeeze("columns")
y_test = pd.read_csv("data/splits/y_test.csv").squeeze("columns")

# Initialize Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)

print("AGRIPAK - RANDOM FOREST MODEL TRAINING")
print("=" * 50)

print(f"\nAccuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, predictions))

print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

# Save trained model
joblib.dump(model, "agri_pak_model.pkl")

print("\nRandom Forest model saved successfully!")
