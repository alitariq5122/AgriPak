import pandas as pd
# import matplotlib.pyplot as plt Imports the plotting library
import matplotlib.pyplot as plt
# Load the agricultural dataset
df = pd.read_excel("data/crop_data.xlsx")

# Count the records for each risk category
#sort_index() Keeps categories in order: 0, then 1
risk_counts = df["low_yield_risk"].value_counts().sort_index()

# Create the bar chart
#plt.figure() Sets the chart size
plt.figure(figsize=(7, 5))

#plt.bar() Creates a bar chart
plt.bar(
    ["Risk 0", "Risk 1"],
    risk_counts.values
)

# Display exact values above each bar
# enumerate() gets each bar's position and value.
# plt.text() displays text on the chart.
# i represents the horizontal position.
# value represents the height of the bar.
# ha="center" centers the number.
# va="bottom" places it just above the bar.
for i, value in enumerate(risk_counts.values):
    plt.text(i, value, str(value), ha="center", va="bottom")

# Add chart labels and title
plt.title("Low-Yield Risk Distribution")
plt.xlabel("Low-Yield Risk Category")
plt.ylabel("Number of Records")

# Display the chart
# plt.tight_layout() automatically adjusts the spacing in your chart so that its elements don't overlap or get cut off.
plt.tight_layout()
plt.show()

# =================================
# RAINFALL DISTRIBUTION
# =================================

# Create a new figure
plt.figure(figsize=(7, 5))

# Create histogram which shows 
# df["rainfall_mm"] selects the rainfall column.
# bins=20 divides rainfall values into 20 intervals.
# edgecolor="black" adds borders to the bars.
# Frequency shows how many records fall into each rainfall interval.
plt.hist(df["rainfall_mm"], bins=20, edgecolor="black")

# Add chart labels and title
plt.title("Rainfall Distribution")
plt.xlabel("Rainfall (mm)")
plt.ylabel("Frequency")

# Adjust layout and display chart
plt.tight_layout()
plt.show()