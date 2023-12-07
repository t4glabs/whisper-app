import streamlit as st
from pymongo import MongoClient
import whisper_transcriber
import whisperX_transcriber
from whisper_translator import translate_audio
from utils.file_uploader import upload_file
import tempfile
from dotenv import load_dotenv
from urllib.parse import quote_plus
import os

load_dotenv()

host = os.getenv("MONGO_HOST")
username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")
database_name = os.getenv("MONGO_DATABASE_NAME")
collection_name = os.getenv("MONGO_COLLECTION_NAME")


def init_mongo_client():
    # URL-encode the username and password
    username_encoded = quote_plus(username)
    password_encoded = quote_plus(password)

    connection_string = f"mongodb+srv://{username_encoded}:{password_encoded}@{host}/{database_name}?retryWrites=true&w=majority"
    client = MongoClient(connection_string)
    return client[database_name][collection_name]

mongo_client = init_mongo_client()

def user_login():
    st.title('Login')
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        user = mongo_client.find_one({"username": username, "password": password})
        if user:
            st.success("Login Successful!")
            return True
        else:
            st.error("Invalid username or password")
    return False

def user_logout():
    st.session_state['logged_in'] = False
    st.rerun()  

def main():
    if not st.session_state.get('logged_in', False):
        if user_login():
            st.session_state['logged_in'] = True

    if st.session_state.get('logged_in', False):
        # Main page content
        st.title('Audio Transcription App')
        st.write('Upload your audio file and choose your transcription service.')

        audio_file = upload_file()
        if audio_file is not None:
            tfile = tempfile.NamedTemporaryFile(delete=False, suffix=".wav") 
            tfile.write(audio_file.read())
            audio_file = tfile.name

        transcription_service = st.selectbox(
            'Choose your transcription service', 
            ('Whisper', 'WhisperX')
        )

        if transcription_service == 'WhisperX':
            whisper_model = st.radio(
                'Choose your Whisper model',
                (
                    'tiny.en', 
                    'tiny', 
                    'base.en', 
                    'base', 
                    'small.en', 
                    'small', 
                    'medium.en', 
                    'medium', 
                    'large-v1', 
                    'large-v2', 
                    'large'
                )
            )

        col1, col2, col3 = st.columns([1, 2, 2])
        transcribe_button = col2.button('Transcribe')
        translate_button = col3.button('Translate')
        
        if transcribe_button:
            if transcription_service == 'Whisper':
                transcription = whisper_transcriber.transcribe_audio(audio_file)
            else:
                transcription = whisperX_transcriber.transcribe_audio(audio_file, whisper_model)

            st.write('Transcription:')
            st.write(transcription)
            
        
        if translate_button and audio_file is not None:
          
            target_language = st.selectbox(
                'Select the language for translation', 
                list(available_languages().keys())
            )

            translation = translate_audio(audio_file, target_language)  # Pass the selected language
            st.write('Translation:')
            st.write(translation)

      
        if st.button("Logout"):
            user_logout()

if __name__ == "__main__":
    main()
