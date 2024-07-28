# MAJOR FLAW: WITH ANY EXPRESSIONS RELATED TO MATH, ALL SYMBOLS MUST BE
# CONVERTED TO THEIR WORD FORM

import os
import requests
from dotenv import load_dotenv

def generate_mp4(voice, message):
    # Load environment variables from .env file
    load_dotenv()

    # Retrieve the environment variables
    PLAY_HT_API_KEY = os.getenv('PLAY_HT_API_KEY')
    PLAY_HT_USER_ID = os.getenv('PLAY_HT_USER_ID')

    if voice == "girl":
        a = "s3://voice-cloning-zero-shot/d9ff78ba-d016-47f6-b0ef-dd630f59414e/female-cs/manifest.json"
    else:
        a = "s3://mockingbird-prod/william_3_d2b62fd7-a52d-4bd1-a09a-fb2748eda979/voices/william_3/manifest.json"
    url = "https://api.play.ht/api/v2/tts"

    payload = {
        "text": message,
        "voice": a,
        "output_format": "mp3",
        "voice_engine": "PlayHT2.0"
    }

    headers = {
        "accept": "text/event-stream",
        "content-type": "application/json",
        "AUTHORIZATION": PLAY_HT_API_KEY,
        "X-USER-ID": PLAY_HT_USER_ID
    }
    response = requests.post(url, json=payload, headers=headers)
    print(response.text)

generate_mp4("girl", "I have a question. What is x plus 7 if x minus 1 is 5?")