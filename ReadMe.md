# AgriPak

## Overview
AgriPak is a Machine Learning project focused on agricultural data analysis and low-yield risk prediction. It uses agricultural data to explore crop and environmental conditions and develop models that classify potential low-yield risks.

## Objectives
- Analyze agricultural datasets.
- Explore important crop and environmental features.
- Perform data preprocessing and visualization.
- Develop machine learning classification models.
- Compare model performance to identify the better-performing model.

## Dataset
The project uses an agricultural dataset containing **50,000 records and 10 columns**.

### Features
- Region
- Soil Type
- Crop
- Rainfall (mm)
- Temperature (°C)
- Fertilizer Used
- Irrigation Used
- Weather Condition
- Days to Harvest
- Low-Yield Risk (Target Variable)

## Project Workflow

1. **Data Exploration:** Examining dataset structure, missing values, duplicates, and statistical summaries.
2. **Data Visualization:** Visualizing low-yield risk distribution and rainfall distribution.
3. **Data Preprocessing:** Separating input features and target variable, encoding categorical data using One-Hot Encoding, and splitting the dataset into training and testing sets.
4. **Model Training:** Training Logistic Regression and Random Forest classification models.
5. **Model Evaluation:** Evaluating accuracy, precision, recall, F1-score, and confusion matrices.
6. **Model Comparison:** Comparing both models to identify the better-performing approach.

## Machine Learning Models

- Logistic Regression
- Random Forest Classifier

### Model Comparison Results

| Model | Accuracy |
|---|---:|
| Logistic Regression | 91.88% |
| Random Forest | 91.61% |

**Selected Model:** Logistic Regression, based on its slightly higher accuracy and recall for the low-yield-risk class.

## Technologies and Libraries

- Python
- Pandas
- Matplotlib
- Scikit-learn
- OpenPyXL
- Joblib

## Project Structure

```text
AgriPak/
│
├── data/
│   └── crop_data.xlsx
│
├── src/
│   ├── data_exploration.py
│   ├── data_visualization.py
│   ├── data_preprocessing.py
│   ├── model_training.py
│   └── model_comparison.py
│
├── agri_pak_model.pkl
├── README.md
├── LICENSE
└── .gitignore
```

## Project Status

Initial machine learning development completed, including data exploration, visualization, preprocessing, model training, evaluation, and model comparison.