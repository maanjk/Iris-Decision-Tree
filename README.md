# Iris Decision Tree Classifier – Kaggle + Streamlit

This project demonstrates a complete end‑to‑end machine learning workflow:

1. Train and evaluate a **Decision Tree classifier** on the classic Iris dataset using **Kaggle**.
2. Deploy an interactive **Streamlit** web app that uses the trained model to predict the Iris species from user‑provided measurements.

---

## Live Demo

Streamlit app (hosted from this GitHub repo):

**https://iris-decision-tree-7r9qmzp4jgpuup2bydsib7.streamlit.app/**

---

## Training Notebook (Kaggle)

The model is trained and evaluated in this Kaggle notebook:

**https://www.kaggle.com/code/musmanaslamawan/iris-decision-tree-train**

The notebook covers:

- Loading the Iris dataset.
- Exploratory data analysis (EDA).
- Train–test split.
- Training a `DecisionTreeClassifier` from `scikit-learn`.
- Evaluating accuracy and other metrics.
- Saving the trained model (or documenting its parameters) for deployment.

---

## Dataset

- **Dataset:** Iris Flower Dataset  
- **Source (Kaggle):** https://www.kaggle.com/datasets/arshid/iris-flower-dataset  
- **Task type:** Multi‑class classification (3 classes)  
- **Features:**
  - `sepal_length` (cm)
  - `sepal_width` (cm)
  - `petal_length` (cm)
  - `petal_width` (cm)
- **Target (label):**
  - Iris species: `setosa`, `versicolor`, `virginica`

---

## Model

- **Algorithm:** Decision Tree Classifier (`sklearn.tree.DecisionTreeClassifier`)
- **Key idea:**  
  The decision tree learns simple decision rules based on the four flower measurements to classify each sample into one of the three Iris species.

The Kaggle notebook experiments with:

- Train/test split (e.g., 80/20).
- Tree depth and other hyperparameters.
- Evaluation using accuracy, confusion matrix, and classification report.

---

## Streamlit Web App

The Streamlit app provides a simple user interface where you can move sliders to input flower measurements and get an instant prediction.

### Features

- Sliders for:
  - Sepal length (cm)
  - Sepal width (cm)
  - Petal length (cm)
  - Petal width (cm)
- “Predict” button to run the Decision Tree classifier.
- Displays the predicted Iris species.

---

## Running the App Locally

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/iris-decision-tree.git
cd iris-decision-tree
