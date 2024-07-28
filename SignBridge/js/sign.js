
// Mock function to update output area
function updateOutputArea(text) {
    var outputArea = document.getElementById("outputArea");
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
