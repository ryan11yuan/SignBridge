from flask import Flask, request, jsonify
import cv2
import numpy as np
import os

app = Flask(__name__)


@app.route('/process_video', methods=['POST'])
def process_video():
    if 'video' not in request.files:
        return 'No video file', 400

    video_file = request.files['video']
    video_path = 'temp_video.webm'
    video_file.save(video_path)

    # Process the video here
    detected_text = detect_sign_language(video_path)

    # Clean up the temporary video file
    os.remove(video_path)

    return jsonify({'detected_text': detected_text})


def detect_sign_language(video_path):
    # Load the video file
    cap = cv2.VideoCapture(video_path)

    # Placeholder for processing frames and detecting sign language
    # Replace this with your actual sign language detection logic
    detected_text = "Example detected text"

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # Process each frame (placeholder)
        # For example, you could call your ML model here
        # detected_text = your_model.predict(frame)

    cap.release()
    return detected_text


if __name__ == '__main__':
    app.run(debug=True)
