let mediaRecorder;
let recordedChunks = [];

const videoElement = document.getElementById('videoElement');
const startButton = document.getElementById('startButton');
const stopButton = document.getElementById('stopButton');
const outputArea = document.getElementById('outputArea');

startButton.addEventListener('click', startRecording);
stopButton.addEventListener('click', stopRecording);

async function startRecording() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
        videoElement.srcObject = stream;

        mediaRecorder = new MediaRecorder(stream);

        mediaRecorder.ondataavailable = (event) => {
            if (event.data.size > 0) {
                recordedChunks.push(event.data);
            }
        };

        mediaRecorder.start();
        startButton.disabled = true;
        stopButton.disabled = false;
        outputArea.textContent = 'Recording...';
    } catch (error) {
        console.error('Error accessing media devices:', error);
        outputArea.textContent = 'Error accessing camera and microphone.';
    }
}

function stopRecording() {
    mediaRecorder.stop();
    startButton.disabled = false;
    stopButton.disabled = true;
    outputArea.textContent = 'Processing...';

    mediaRecorder.onstop = () => {
        const blob = new Blob(recordedChunks, { type: 'video/webm' });
        sendRecordingToPython(blob);
        recordedChunks = [];
    };
}

function sendRecordingToPython(blob) {
    const formData = new FormData();
    formData.append('video', blob, 'recording.webm');

    fetch('/process_video', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(result => {
        outputArea.textContent = 'Detected text: ' + result;
    })
    .catch(error => {
        console.error('Error sending video to server:', error);
        outputArea.textContent = 'Error processing video.';
    });
}
