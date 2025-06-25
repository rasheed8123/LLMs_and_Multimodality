# 📊 Model Output Comparisons

A set of prompts tested across all three model types.

---

## ✅ Prompt Set

1. Describe the lifecycle of a butterfly in simple words.
2. What is quantum entanglement?
3. Write a short story about a robot learning emotions.
4. Explain photosynthesis to a 6th grader.
5. What are the pros and cons of online education?

---

## 📋 Results Table

| Prompt | Model Type | Output (Summary) | Tokens (optional) | Notes |
|--------|------------|------------------|--------------------|-------|
| Butterfly lifecycle | Base (TinyLLaMA) | ... | ... | ... |
|  | Instruct (Mistral) | ... | ... | ... |
|  | Fine-tuned (GPT-4) | Clear, structured | 110 | Best tone |

---

## 💡 Commentary

- **Base (TinyLLaMA)**: Useful for raw testing or fine-tuning, but needs clear prompts.
- **Instruct (Mistral)**: Reliable for instruction-following and natural language outputs.
- **Fine-tuned (GPT-4)**: Strongest for user-friendly tone, polish, and context awareness.

---

## 🧠 When to Use What?

| Scenario | Best Model |
|----------|------------|
| Quick local inference | TinyLLaMA |
| General-purpose assistant | Mistral |
| Custom brand tone or detailed reasoning | GPT-4 Fine-tuned |