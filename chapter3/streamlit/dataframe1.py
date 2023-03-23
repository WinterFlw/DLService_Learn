import streamlit as st
import numpy as np

df = np.random.randn(10, 20)
st.dataframe(df)
