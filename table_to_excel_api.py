import streamlit as st
import requests
# st.title('Table to excel API')
TYPES = ['Accessible', 'Scanned', 'Image']

st.header('Table to excel API')
st.subheader('Coming soon')

# with st.container(border=True):
#     role = st.selectbox("Document Type", TYPES)

#     uploaded_file = st.file_uploader(
#         "Choose a file", accept_multiple_files=False
#     )

# if st.button("Execute"):
#     bytes_data = uploaded_file.read()

# def post_data(type):
#     with st.spinner("Working..."):
#         ### prepare API key and URL
#         api_key = st.secrets["API_KEY"]
#         api_url = f"https://api.api-ninjas.com/v1/{type}"

#         ### invoke API and get the response
#         response = requests.post(url=api_url, headers={"X-Api-Key": api_key})
#         if response.status_code == requests.codes.ok:
#             ### Convert data to JSON format
#             data = jsonify(response)
#             status = "OK"
#         else:
#             data = {"code": response.status_code, "message": response.text}
#             status = "ERROR"
#     return status, data