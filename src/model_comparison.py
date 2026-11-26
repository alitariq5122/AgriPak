
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

# Load the saved training and testing datasets
X_train = pd.read_csv("data/splits/X_train.csv")
X_test = pd.read_csv("data/splits/X_test.csv")
y_train = pd.read_csv("data/splits/y_train.csv").squeeze("columns")
y_test = pd.read_csv("data/splits/y_test.csv").squeeze("columns")

# Initialize models
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
}

results = []

print("AGRIPAK - MODEL COMPARISON")
print("=" * 50)

# Train and evaluate each model
for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)

    results.append({
        "Model": name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1-Score": f1
    })

    print(f"\n{name}")
    print("-" * 40)
    print(f"Accuracy:  {accuracy * 100:.2f}%")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1-Score:  {f1:.4f}")

    print("\nClassification Report:")
    print(classification_report(y_test, predictions))

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, predictions))

# Display final comparison
comparison = pd.DataFrame(results)

print("\nFINAL MODEL COMPARISON")
print("=" * 50)
print(comparison.to_string(index=False))

# Save comparison results
comparison.to_csv("data/model_comparison_results.csv", index=False)

print("\nComparison results saved successfully!")
