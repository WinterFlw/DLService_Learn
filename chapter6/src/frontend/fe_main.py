# frontend/fe_main.py

import requests
import streamlit as st
from PIL import Image

import json
import boto3
from botocore.config import Config


def query_endpoint(img):

    my_config = Config(
        region_name = 'ap-northeast-2'
    )

    endpoint_name = 'cat-breed-ep-sync'
    client = boto3.client('runtime.sagemaker', config=my_config)
    response = client.invoke_endpoint(EndpointName=endpoint_name, ContentType='application/x-image', Body=img, Accept='application/json;verbose')
    return response

def parse_prediction(query_response):
    model_predictions = json.loads(query_response['Body'].read())
    labels = model_predictions['labels']
    probabilities = [round(p,2) for p in model_predictions['probabilities']]
    labels_probs = dict(zip(labels, probabilities))

    return labels_probs

# https://discuss.streamlit.io/t/version-0-64-0-deprecation-warning-for-st-file-uploader-decoding/4465
st.set_option("deprecation.showfileUploaderEncoding", False)

# defines an h1 header
st.title("Cat breed Classification API Test")

# displays a file uploader widget
image = st.file_uploader("Choose an image")

# displays a button
if st.button("Prediction"):
    if image is not None:
        headers={"Content-Type": "application/x-image"}
        res = query_endpoint(image.getvalue())
        result = parse_prediction(res)
        st.write(result)
        st.image(image.getvalue(), width=240)
