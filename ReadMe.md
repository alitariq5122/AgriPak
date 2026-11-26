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
│   ├── crop_data.xlsx
│   ├── crop_data.csv
│   ├── crop_data_cleaned.csv
│   ├── feature_correlations.csv
│   └── splits/
│       ├── X_train.csv
│       ├── X_test.csv
│       ├── y_train.csv
│       └── y_test.csv
│
├── notebooks/
│
├── src/
│   ├── data_exploration.py
│   ├── data_visualization.py
│   ├── data_cleaning.py
│   ├── data_preprocessing.py
│   ├── leakage_check.py
│   ├── model_training.py
│   └── model_comparison.py
│
├── agri_pak_model.pkl
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## Project Status

Initial machine learning development completed, including data exploration, visualization, preprocessing, model training, evaluation, and model comparison.

## Data Cleaning

The dataset was checked for missing values, duplicate records, and appropriate data types.

- Original dataset: 50,000 records and 10 columns.
- Missing values: None found.
- Duplicate records: None found.
- Numerical and categorical data types were checked and converted where appropriate.
- No records required removal or missing-value imputation.

The cleaned dataset was saved as `data/crop_data_cleaned.csv`.

## Train-Test Split

The cleaned dataset was divided using stratified sampling:

- Training set: 80% (40,000 records).
- Testing set: 20% (10,000 records).
- Random state: 42.
- Stratification: Applied using the target variable.

The four split files are saved in `data/splits/`.

## Leakage Sanity Check

Pearson correlation was calculated between all input features and the target variable `low_yield_risk`.

Categorical features were converted into one-hot encoded columns before calculating correlations.

**Results:**
- Total features checked: 24.
- Numerical features: 5.
- One-hot encoded categorical features: 19.
- Features exceeding the absolute correlation threshold of 0.9: None.

**Highest absolute correlation:**

| Feature | Correlation |
|---|---:|
| rainfall_mm | -0.636409 |

No features exceeded the absolute correlation threshold of 0.9. Therefore, no features were flagged for potential leakage based on this correlation check.

All correlation results are saved in `data/feature_correlations.csv`.

*Note: This correlation check does not guarantee that the dataset is completely free from data leakage. Further investigation of feature timing and target generation may be required.*

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/alitariq5122/AgriPak.git
cd AgriPak
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Project Scripts

Run the scripts from the project root directory:

```bash
python src/data_exploration.py
python src/data_visualization.py
python src/data_cleaning.py
python src/data_preprocessing.py
python src/leakage_check.py
python src/model_training.py
python src/model_comparison.py
```

**Note:** The dataset must be available in the `data/` directory before running the scripts.