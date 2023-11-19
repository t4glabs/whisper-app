import streamlit as st

def upload_file():
    uploaded_file = st.file_uploader("Choose an audio file", type=['wav', 'mp3', 'flac'], key="file-uploader")
    if uploaded_file is not None:
        return uploaded_file
    else:
        st.write("Please upload an audio file.")
        return None