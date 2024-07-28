import os
import websockets
import asyncio
from openai import OpenAI
from generate_notes import *

def transcribe(file_path):
    api_key = os.getenv('OPENAI_API_KEY')
    client = OpenAI(api_key=api_key)
    with open(file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return send_prompt(transcription.text, 3, 3)

async def handle_client(websocket, path):
    
    # Path to your audio file
    file_path = r"speech/SignBridge.mp3"

    await websocket.send(transcribe(file_path))
    print(f"Sent transcription: {transcribe(file_path)}")
    
    await asyncio.sleep(0.01)

start_server = websockets.serve(handle_client, "localhost", 8766)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

