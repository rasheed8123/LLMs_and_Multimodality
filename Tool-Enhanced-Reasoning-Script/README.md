# 🤖 Tool-Enhanced Reasoning Script

This project demonstrates how to combine LLM-based reasoning (via OpenAI) with external tools to answer natural language queries more effectively.

## 📦 Features

- Uses OpenAI’s GPT model for step-by-step (Chain-of-Thought) reasoning
- Detects and calls external Python functions (tools) only when needed
- Outputs reasoning, tool used, and final answer
- Lightweight and framework-free (no LangChain or agents)

---

## 🛠️ Tools Implemented

### Math Tools (`tools/math_tools.py`)
- `average(numbers: List[int])` — Calculates average
- `square_root(x: float)` — Computes square root

### String Tools (`tools/string_tools.py`)
- `count_vowels(word: str)` — Counts vowels in a word
- `count_letters(word: str)` — Counts alphabetic letters

---

## 💬 Example Queries

| Query | Tool Used | Final Output |
|-------|-----------|--------------|
| What’s the square root of the average of 18 and 50? | ✅ `average()` + `square_root()` | ≈ 5.83 |
| How many vowels are in the word ‘Multimodality’? | ✅ `count_vowels()` | 5 |
| Is the number of letters in ‘machine’ greater than the number of vowels in ‘reasoning’? | ✅ `count_letters()` vs `count_vowels()` | `True` |
| Add 23 and 42 together. | ❌ Tool not used | 65 |
| How many letters are in ‘Thoughtfulness’? | ✅ `count_letters()` | 13 |

---

## 📂 Directory Structure

Tool-Enhanced-Reasoning-Script/
├── main.py
├── tools/
│ ├── math_tools.py
│ └── string_tools.py
├── .env.example
├── requirements.txt
└── README.md

yaml

---

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash

cd Tool-Enhanced-Reasoning-Script
2. Install Dependencies
bash

pip install -r requirements.txt
3. Add API Key
bash

cp .env.example .env
# Then open .env and paste your OpenAI key
ini

OPENAI_API_KEY=your-openai-api-key-here
4. Run the Script
bash

python main.py
🧠 Prompt Strategy
We use a static prompt like:

vbnet

Answer the question step-by-step. If tool usage is needed, describe the steps clearly.
This encourages the LLM to:

Think logically and explicitly (Chain-of-Thought)

Output phrases like "find average" or "count vowels" — which we match to tools
