import os
import requests


def send_prompt(question_text, pages, detailed_level):
    api_key = os.getenv('OPENAI_API_KEY')
    url = "https://api.openai.com/v1/chat/completions"

    # Define the headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Construct the question with the specified details
    question = (
        f"Please summarize the following text in note form, "
        f"ensuring it is concise, clear, and fits into {pages} pages. "
        f"Include the level of detail: {detailed_level} out of 5. Please also style it __ \n\n"
        f"{question_text}"
    )

    # Define the payload
    payload = {
        "model": "gpt-4",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    }

    # Make the POST request
    response = requests.post(url, headers=headers, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON to get the answer
        answer = response.json()['choices'][0]['message']['content']
        return answer
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)
        return None