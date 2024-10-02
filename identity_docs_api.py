import streamlit as st
import requests
import constants
import os
import json

# st.title('Table to excel API')
TYPES = {
    'Aadhar card': 'aadhar', 
    'Pan card': 'pan', 
    'Passport': 'passport', 
    'Driving license': 'driving_license', 
    'Voter ID': 'voter_id'
}

st.header('Identity docs API')
st.subheader('Extract information from identity documents such as Aadhar, PAN, Passport, etc.')

def post_data(type, file):
    with st.spinner("Working..."):
        api_url = f"{constants.BASE_URL}{constants.IDENTITY_ENDPOINT}"
        params = {
            'document_type': TYPES[type]
        }
        files = {
            'image': (file.name, file, 'image/jpeg')
        }
        response = requests.post(url=api_url, params=params, files=files)
        if response.status_code == requests.codes.ok:
            status = "OK"
            data = response.text
        else:
            data = {"code": response.status_code, "message": response.text}
            status = "ERROR"
    return status, data

@st.dialog("Response", width='large')
def response_dialog(response):
    st.json(json.loads(response), expanded=True)

with st.container(border=True):
    type = st.selectbox("Document Type", TYPES.keys())

    uploaded_file = st.file_uploader(
        "Choose an image file", accept_multiple_files=False, type=['jpg', 'png', 'jpeg']
    )

if st.button("Execute"):
    if uploaded_file is not None:
        status, response = post_data(type, uploaded_file)
        st.subheader('Response')
        st.write(status)
        with st.container(border=True):
            st.json(json.loads(response), expanded=True)