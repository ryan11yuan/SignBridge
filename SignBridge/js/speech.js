function goHome() {
    window.location.href = "index.html"; 
}

const outputElement = document.getElementById('output');
const ws = new WebSocket('ws://localhost:8766');

ws.onmessage = (event) => {
    console.log(event.data)
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