import os
from openai import OpenAI
from dotenv import load_dotenv
from tools.math_tools import average, square_root
from tools.string_tools import count_vowels, count_letters

# Load API key from .env
load_dotenv()
client = OpenAI()  # Automatically reads OPENAI_API_KEY from environment

def call_llm(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant that thinks step-by-step and calls tools if needed."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


def tool_selector(reasoning):
    reasoning_lower = reasoning.lower()
    if "square root" in reasoning_lower and "average" in reasoning_lower:
        return "math_average_sqrt"
    elif "vowels" in reasoning_lower:
        return "count_vowels"
    elif "letters" in reasoning_lower:
        return "compare_letters_vowels"
    return None


def process_query(query):
    print(f"\n🔍 Query: {query}")
    prompt = f"Answer the question step-by-step. If tool usage is needed, describe the steps clearly.\n\nQuery: {query}"
    reasoning = call_llm(prompt)
    print(f"\n🧠 Reasoning:\n{reasoning}")

    tool = tool_selector(reasoning)
    print(f"\n🛠️ Tool Selected: {tool if tool else 'None'}")

    if tool == "math_average_sqrt":
        numbers = [int(s) for s in query.split() if s.isdigit()]
        result = square_root(average(numbers))
    elif tool == "count_vowels":
        word = query.split("‘")[1]
        result = count_vowels(word)
    elif tool == "compare_letters_vowels":
        words = [w.strip("‘’") for w in query.split("‘")[1::2]]
        if len(words) == 2:
           result = count_letters(words[0]) > count_vowels(words[1])
        elif len(words) == 1:
           result = count_letters(words[0])
        else:
           result = "Could not parse words properly."

    else:
        result = "Tool not needed or not recognized."

    print(f"\n✅ Final Answer: {result}\n")
    return reasoning, tool, result


if __name__ == "__main__":
    test_queries = [
        "What’s the square root of the average of 18 and 50?",
        "How many vowels are in the word ‘Multimodality’?",
        "Is the number of letters in ‘machine’ greater than the number of vowels in ‘reasoning’?",
        "Add 23 and 42 together.",
        "How many letters are in ‘Thoughtfulness’?"
    ]

    for query in test_queries:
        process_query(query)
