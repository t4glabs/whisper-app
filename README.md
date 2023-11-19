# My Streamlit App

This is a Streamlit app that uses the Whisper and WhisperX ASR APIs to transcribe audio files into text. The app also provides an option to translate the transcribed text into a different language using the Whisper ASR API.

## Installation

1. Clone this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Install the required Python packages using the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app using the following command:

```bash
streamlit run src/main.py
```

2. The app will open in your default web browser. You can also manually navigate to the app by entering the following URL into your web browser's address bar:

```bash
http://localhost:8501
```

3. Use the file upload option to upload an audio file that you want to transcribe.
4. Choose whether you want to use Whisper or WhisperX for transcription.
5. The transcribed text will be displayed on the screen.
6. If you want to translate the transcribed text into a different language, select the desired language from the dropdown menu and click the 'Translate' button.
