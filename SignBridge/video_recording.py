from flask import Flask, request, jsonify
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/process_video', methods=['POST'])
def process_video():
    if 'video' not in request.files:
        return 'No video file', 400

    video_file = request.files['video']
    video_path = 'temp_video.webm'
    video_file.save(video_path)

    # Process the video here
    # This is a placeholder for your sign language detection logic
    result = "Example detected text"

    return result

if __name__ == '__main__':
    app.run(debug=True)