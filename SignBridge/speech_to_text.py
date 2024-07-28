import os
from openai import OpenAI
from generate_notes import *

def transcribe(file_path):
    api_key = os.getenv('OPENAI_API_KEY')
    # Initialize the OpenAI client with the API key
    client = OpenAI(api_key=api_key)
    with open(file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return send_prompt(transcription.text, 3, 3)

# Path to your audio file
file_path = r"C:\Users\willp\Documents\GitHub\SignBridge\OSR_us_000_0010_8k.wav"

# Perform transcription
print(transcribe(file_path))
