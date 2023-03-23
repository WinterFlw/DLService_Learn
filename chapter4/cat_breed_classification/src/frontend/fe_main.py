# frontend/main.py

import requests
import streamlit as st
from PIL import Image

# https://discuss.streamlit.io/t/version-0-64-0-deprecation-warning-for-st-file-uploader-decoding/4465
st.set_option("deprecation.showfileUploaderEncoding", False)

# defines an h1 header
st.title("Cat breed Classification API Test")

# displays a file uploader widget
image = st.file_uploader("Choose an image")

# displays a button
if st.button("Prediction"):
    if image is not None:
        files = {"file": image.getvalue()}
        headers={"Content-Type": "multipart/form-data"}
        res = requests.post(f"http://127.0.0.1:8000/detect_labels",  files=files)
        st.write(str(res.json()))
        st.image(image.getvalue(), width=240)
