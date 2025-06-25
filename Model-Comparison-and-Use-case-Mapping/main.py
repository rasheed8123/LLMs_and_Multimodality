# src/main.py

import argparse

# Import model functions (we'll implement them step-by-step)
from models.local_model import query_tinyllama
from models.mistral_model import query_mistral
from models.openai_model import query_openai
from utils.model_summary import get_model_summary


def main():
    parser = argparse.ArgumentParser(description="Compare LLMs: Base, Instruct, and Fine-tuned")
    parser.add_argument(
        "--model-type",
        choices=["base", "instruct", "fine-tuned"],
        required=True,
        help="Choose model type: base (TinyLLaMA), instruct (Mistral), or fine-tuned (OpenAI)"
    )
    parser.add_argument(
        "--prompt",
        type=str,
        required=True,
        help="The input prompt to send to the model"
    )

    args = parser.parse_args()
    model_type = args.model_type
    prompt = args.prompt

    # Dispatch to appropriate model
    if model_type == "base":
        response = query_tinyllama(prompt)
        model_name = "TinyLLaMA"
    elif model_type == "instruct":
        response = query_mistral(prompt)
        model_name = "Mistral-7B-Instruct"
    elif model_type == "fine-tuned":
        response = query_openai(prompt)
        model_name = "OpenAI Fine-tuned (GPT-4 Turbo)"
    else:
        raise ValueError("Invalid model type")

    # Print the results
    print("\n" + "=" * 60)
    print(f"🧠 Model Used: {model_name}")
    print(get_model_summary(model_name))
    print("-" * 60)
    print(f"📤 Response:\n{response}")
    print("=" * 60)


if __name__ == "__main__":
    main()
