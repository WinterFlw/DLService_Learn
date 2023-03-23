import streamlit as st
from io import StringIO
import pandas as pd

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
     # To read file as bytes:
     bytes_data = uploaded_file.getvalue()
     st.image(bytes_data)