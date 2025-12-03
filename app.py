import numpy as np
import joblib
import streamlit as st

# Load the trained model
model = joblib.load("iris_dt_model.pkl")

st.title("Iris Flower Classifier (Decision Tree)")

st.write("Enter flower measurements to predict the Iris species:")

sepal_length = st.slider("Sepal length (cm)", 4.0, 8.0, 5.1, 0.1)
sepal_width  = st.slider("Sepal width (cm)",  2.0, 4.5, 3.5, 0.1)
petal_length = st.slider("Petal length (cm)", 1.0, 7.0, 1.4, 0.1)
petal_width  = st.slider("Petal width (cm)",  0.1, 2.5, 0.2, 0.1)

if st.button("Predict"):
    x = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    pred = model.predict(x)[0]
    st.success(f"Predicted species: {pred}")