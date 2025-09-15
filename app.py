import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open('diamond_randomforest.pkl', 'rb'))

st.title("Diamond Price Prediction")

carat = st.number_input("Carat", min_value=0.0, max_value=10.0, value=0.5)
cut = st.selectbox("Cut", ["Fair", "Good", "Very Good", "Premium", "Ideal"])
color = st.selectbox("Color", ["D", "E", "F", "G", "H", "I", "J"])
clarity = st.selectbox("Clarity", ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"])
depth = st.number_input("Depth", min_value=0.0, max_value=100.0, value=61.5)
table = st.number_input("Table", min_value=0.0, max_value=100.0, value=55.0)
x = st.number_input("X (mm)", min_value=0.0, max_value=10.0, value=5.0)
y = st.number_input("Y (mm)", min_value=0.0, max_value=10.0, value=5.0)
z = st.number_input("Z (mm)", min_value=0.0, max_value=10.0, value=3.0)

input_data = pd.DataFrame({
    'carat':[carat],
    'cut':[cut],
    'color':[color],
    'clarity':[clarity],
    'depth':[depth],
    'table':[table],
    'x':[x],
    'y':[y],
    'z':[z]
})

if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Diamond Price: ${prediction[0]:.2f}")