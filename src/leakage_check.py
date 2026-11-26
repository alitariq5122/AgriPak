
import pandas as pd

# Load cleaned agricultural dataset
df = pd.read_csv("data/crop_data_cleaned.csv")

# Separate target variable from input features
y = df["low_yield_risk"]
X = df.drop("low_yield_risk", axis=1)

# Convert categorical features into numerical columns
X_encoded = pd.get_dummies(
    X,
    columns=["region", "soil_type", "crop", "weather_condition"],
    dtype=int
)

# Calculate Pearson correlation for every encoded feature
correlations = X_encoded.corrwith(y)

# Display correlation results
print("AGRIPAK - COMPLETE LEAKAGE SANITY CHECK")
print("=" * 50)

print("\nFeature Correlations with Low-Yield Risk:")
print(correlations.sort_values(ascending=False).to_string())

# Flag features with absolute correlation above 0.9
flagged_features = correlations[correlations.abs() > 0.9]

print("\nFEATURES WITH ABSOLUTE CORRELATION ABOVE 0.9")
print("=" * 50)

if flagged_features.empty:
    print("No features exceeded the correlation threshold of 0.9.")
else:
    print(flagged_features)

# Save all correlation results
correlations.sort_values(ascending=False).to_csv(
    "data/feature_correlations.csv",
    header=["correlation"]
)

print("\nTotal features checked:", len(correlations))
print("Flagged features:", len(flagged_features))
print("\nComplete correlation results saved successfully!")
