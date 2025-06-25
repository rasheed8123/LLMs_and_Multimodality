
# utils/model_summary.py

def get_model_summary(model_name):
    summaries = {
        "TinyLLaMA": """
🧱 TinyLLaMA (Base Model)
- Type: Base (not instruction-tuned)
- Size: ~110M parameters
- Trained on: Raw web data
- Usage: Requires carefully crafted prompts
- Context Length: ~2048 tokens
""",
        "Mistral-7B-Instruct": """
🎓 Mistral-7B-Instruct
- Type: Instruct-tuned (SFT)
- Size: 7B parameters
- Trained to follow instructions & chat
- Usage: Great for summarization, QA, reasoning
- Context Length: 8192 tokens
""",
        "OpenAI Fine-tuned (GPT-4 Turbo)": """
✨ GPT-4 Turbo (Fine-tuned)
- Type: OpenAI fine-tuned on proprietary data
- Size: >100B parameters (estimated)
- Strongest reasoning, refined tone control
- Usage: Best for custom tone, high accuracy tasks
- Context Length: 128k tokens
"""
    }

    return summaries.get(model_name, "No summary available for this model.")
