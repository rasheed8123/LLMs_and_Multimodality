# 🤖 LLM Model Comparison CLI

A command-line tool to compare responses from different types of language models — Base, Instruct, and Fine-tuned — across popular providers like OpenAI and local models via Ollama.

---

## ✨ Features

- Compare 3 model types:
  - **Base**: TinyLLaMA (local via Ollama)
  - **Instruct**: Mistral 7B (local via Ollama)
  - **Fine-tuned**: OpenAI GPT-4 Turbo (via API)
- Consistent prompt interface
- Model capability summaries
- Supports `.env` config for secure API usage

---

## 🏗️ Requirements

- Python 3.9+
- Ollama installed with `mistral` and `tinyllama` models pulled
- OpenAI API key (for fine-tuned usage)

---

## 🔧 Setup

### 1. Clone the repo

```bash

cd model-comparator-cli
2. Install dependencies

pip install -r requirements.txt
3. Configure API key
Create a .env file in the project root:


cp .env.example .env
Then open .env and add your OpenAI key:

env

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
🚀 Usage
CLI format

python main.py --model-type [base|instruct|fine-tuned] --prompt "Your question here"
Examples

python main.py --model-type base --prompt "Explain gravity like I'm 5"
python main.py --model-type instruct --prompt "Summarize the French Revolution"
python main.py --model-type fine-tuned --prompt "What is the lifecycle of a butterfly?"
📊 Model Summary
Type	Model	Provider	Instruction Tuned	Ideal Use Case
Base	TinyLLaMA	Local	❌	Raw model benchmarking, minimal tasks
Instruct	Mistral 7B	Local	✅	General-purpose reasoning & QA
Fine-tuned	GPT-4 Turbo (OpenAI)	OpenAI	✅✅ (with RLHF/SFT)	Polished tone, domain adaptation

📂 Project Structure

.
├── main.py
├── models/
│   ├── local_model.py
│   ├── mistral_model.py
│   └── openai_model.py
├── utils/
│   └── model_summary.py
├── .env.example
├── README.md
├── requirements.txt
└── comparisons.md
🧠 Related Concepts
Base vs Instruct vs Fine-tuned LLMs

Prompt Engineering

Tokenization and Context Windows

Local vs API-based inference

