# src/models/mistral_model.py

import requests

def query_mistral(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json().get("response", "").strip()
    else:
        return f"[Mistral] Error: {response.status_code} - {response.text}"
