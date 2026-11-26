import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix

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

# Train Logistic Regression
logistic_model = LogisticRegression(max_iter=1000)
logistic_model.fit(X_train, y_train)

# Train Random Forest
random_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
random_model.fit(X_train, y_train)

# Make predictions
logistic_pred = logistic_model.predict(X_test)
random_pred = random_model.predict(X_test)

# Calculate accuracy
logistic_accuracy = accuracy_score(y_test, logistic_pred)
random_accuracy = accuracy_score(y_test, random_pred)

# Display comparison
print("AGRI PAK - MODEL COMPARISON")
print("=" * 40)

print("Logistic Regression Accuracy:",
      round(logistic_accuracy * 100, 2), "%")

print("Random Forest Accuracy:",
      round(random_accuracy * 100, 2), "%")

print("\nLOGISTIC REGRESSION CLASSIFICATION REPORT")
print(classification_report(y_test, logistic_pred))

print("\nLOGISTIC REGRESSION CONFUSION MATRIX")
print(confusion_matrix(y_test, logistic_pred))