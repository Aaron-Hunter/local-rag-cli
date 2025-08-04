import requests

def call_llama(prompt, model="llama3.1:8b", temperature=0.2):
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": model,
        "prompt": prompt,
        "temperature": temperature,
        "stream": False,
    })
    parsed_response = response.json()
    return parsed_response['response']