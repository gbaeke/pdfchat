import streamlit as st
import os

st.title("Upload your PDF")

# Allow user to upload a file
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

# If no file is uploaded, allow user to select a file from a folder
if uploaded_file:
    # save the file to the uploads folder
    try:
        with open(os.path.join("uploads", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
    except Exception as e:
        st.error(e)

    
