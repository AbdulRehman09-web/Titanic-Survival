# Titanic Survival Prediction

This project predicts the survival of passengers on the Titanic using multiple machine learning and deep learning models. It includes data preprocessing, exploratory data analysis (EDA), feature engineering, and model evaluation.

---

## Table of Contents

- [Project Overview](#project-overview)  
- [Dataset](#dataset)  
- [Features](#features)  
- [Models Used](#models-used)  
- [Model Performance](#model-performance)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Results](#results)  
- [License](#license)  

---

## Project Overview

The Titanic dataset is a classic dataset for binary classification tasks. The goal is to predict whether a passenger survived (`1`) or not (`0`) based on various features such as age, gender, passenger class, family size, and fare.  

This project implements the following:

1. **Exploratory Data Analysis (EDA)** using `pandas`, `matplotlib`, and `seaborn`.
2. **Data preprocessing** including handling missing values, encoding categorical features, and scaling numerical features.
3. **Feature engineering**: adding `FamilySize` and `AgeGroup` as features.
4. **Modeling**:  
   - Logistic Regression  
   - Decision Tree  
   - Random Forest  
   - Artificial Neural Network (ANN)  

5. **Model evaluation** using accuracy, precision, recall, F1 score, confusion matrix, and ROC-AUC curves.

---

## Dataset

The dataset used is the Titanic dataset (`Titanic.csv`). Key columns:

- `pclass` — Passenger class (1, 2, 3)  
- `sex` — Gender (0 = female, 1 = male)  
- `age` — Passenger age  
- `sibsp` — Number of siblings/spouses aboard  
- `parch` — Number of parents/children aboard  
- `fare` — Ticket fare  
- `embarked` — Port of embarkation (0=C, 1=Q, 2=S)  
- `survived` — Target variable (0 = Not Survived, 1 = Survived)  

---

## Features

Additional engineered features:

- `FamilySize` = `sibsp + parch + 1`  
- `AgeGroup` (Child, Teen, Adult, MidAge, Senior) — one-hot encoded  
- Numerical features are scaled using `StandardScaler`.  

---

## Models Used

| Model                    | Library        | Description |
|---------------------------|---------------|------------|
| Logistic Regression       | `sklearn`     | Linear classifier for binary classification |
| Decision Tree             | `sklearn`     | Tree-based classifier with max depth 5 |
| Random Forest             | `sklearn`     | Ensemble of decision trees (n_estimators=100) |
| Artificial Neural Network | `keras`       | 3-layer feedforward ANN with ReLU activation, Dropout, and Sigmoid output |

---

## Model Performance

| Model                | Accuracy | Precision | Recall | F1 Score |
|----------------------|---------|----------|--------|----------|
| Logistic Regression  | 0.793   | 0.761    | 0.730  | 0.745    |
| Decision Tree        | 0.799   | 0.828    | 0.649  | 0.727    |
| Random Forest        | 0.827   | 0.803    | 0.770  | 0.786    |
| ANN                  | 0.827   | 0.803    | 0.770  | 0.786    |

The **Random Forest** and **ANN** models achieved the highest accuracy (82.7%).

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/Titanic-Survival.git
cd Titanic-Survival
````

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

1. Ensure the following files are in your working directory:

* `app.py` — Streamlit application
* `best_model.pkl` — Pickled best model (Random Forest or ANN)
* `scaler.pkl`, `scale_cols.pkl`, `feature_cols.pkl` — Preprocessing artifacts

2. Run the Streamlit app:

```bash
streamlit run app.py
```

3. Open your browser at `http://localhost:8501` to input passenger details and get survival predictions.

---

## Results

* Confusion matrices and ROC-AUC curves are generated for each model.
* Feature importance and model evaluation plots are available in the Jupyter notebook version of the project.
* The **best model** (`Random Forest` / `ANN`) is saved as `best_model.pkl` for deployment.

---

## License

This project is licensed under the MIT License.

