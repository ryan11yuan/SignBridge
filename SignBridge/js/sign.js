
// Mock function to update output area
function updateOutputArea(text) {
    var outputArea = document.getElementById("");
    outputArea.textContent = text;
}

// Example usage: Update output area every 2 seconds with a new text
setInterval(function() {
    var mockDetectedText = "Detected sign language text at " + new Date().toLocaleTimeString();
    updateOutputArea(mockDetectedText);
}, 2000);

function goHome() {
    window.location.href = "index.html"; // Replace "index.html" with the actual path to your home page
}

const outputElement = document.getElementById('output');
const ws = new WebSocket('ws://localhost:8766');

ws.onmessage = (event) => {
    outputElement.textContent = event.data;
};

ws.onopen = () => {
    console.log('WebSocket connection established');
};

ws.onclose = () => {
    console.log('WebSocket connection closed');
};

ws.onerror = (error) => {
    console.log('WebSocket error:', error);
};