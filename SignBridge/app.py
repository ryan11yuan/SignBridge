from flask import Flask, request, jsonify
import os
import subprocess
import text_to_speech

app = Flask(__name__)


@app.route('/ask_question', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data.get('question')

    if not question:
        return jsonify({'error': 'No question provided'}), 400

    # Call your text_to_speech.py script here
    response = text_to_speech(question)

    return jsonify({'response': response})


if __name__ == '__main__':
    app.run(debug=True)
