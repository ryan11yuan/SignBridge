const askQuestionButton = document.getElementById('askQuestionButton');
const questionContainer = document.getElementById('questionContainer');
const submitQuestionButton = document.getElementById('submitQuestionButton');
const questionInput = document.getElementById('questionInput');

askQuestionButton.addEventListener('click', () => {
    questionContainer.style.display = 'block';
});

submitQuestionButton.addEventListener('click', () => {
    const question = questionInput.value;
    if (question) {
        sendQuestionToPython(question);
        questionContainer.style.display = 'none';
        questionInput.value = '';
    } else {
        alert('Please enter a question.');
    }
});

function sendQuestionToPython(question) {
    fetch('/ask_question', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question: question }),
    })
    .then(response => response.json())
    .then(data => {
        outputArea.textContent = 'Response: ' + data.response;
    })
    .catch(error => {
        console.error('Error:', error);
        outputArea.textContent = 'Error processing question.';
    });
}
