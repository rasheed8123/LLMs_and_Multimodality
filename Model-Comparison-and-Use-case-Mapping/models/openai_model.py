# models/openai_model.py

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



def query_openai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4",  # Replace with your fine-tuned model name if applicable
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=512
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[OpenAI API] Error:\n\n{e}"
