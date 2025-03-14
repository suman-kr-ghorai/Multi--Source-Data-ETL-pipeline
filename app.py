import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is a simple web app using Streamlit.")

if st.button("Click Me"):
    st.write("You clicked the button!")


name = st.text_input("Enter your name")
st.write(f"Hello, {name}!")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(100, 2)
df = pd.DataFrame(data, columns=["x", "y"])
st.line_chart(df)
