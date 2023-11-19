import whisperx
import dotenv
import os

# load .env file
dotenv.load_dotenv("ops/.env")

YOUR_HF_TOKEN = os.environ.get("HF_TOKEN")

def transcribe_audio(audio_file, model="medium", device="cpu", batch_size=16, compute_type="default"):
    # 1. Transcribe with original whisper (batched)
    model = whisperx.load_model(model, device, compute_type=compute_type)

    audio = whisperx.load_audio(audio_file)
    result = model.transcribe(audio, batch_size=batch_size)

    return result.get("segments", {})[0].get("text", "")

    