import streamlit as st
import whisper_transcriber
import whisperX_transcriber
from whisper_translator import translate_audio
from utils.file_uploader import upload_file
import tempfile

def main():
    st.title('Audio Transcription App')
    st.write(
        'Upload your audio file and choose your transcription service.'
    )

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

    col1, col2, col3 = st.columns([1,2,2])
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
        translation = translate_audio(audio_file)
        st.write('Translation:')
        st.write(translation)

if __name__ == "__main__":
    main()