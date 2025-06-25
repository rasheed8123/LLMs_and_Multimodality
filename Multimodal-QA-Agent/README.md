# 🧠 Multimodal QA Agent (Tkinter + OpenAI GPT-4o)

A simple Python GUI app that allows users to upload an image and ask questions about it using a Vision + Language Large Language Model (LLM).

Built using:
- 🐍 Python
- 🎨 Tkinter (GUI)
- 📷 OpenAI GPT-4o API for image + text understanding

---

## 🚀 Features

- Upload any image (JPG, PNG)
- Ask natural language questions about the image
- Uses OpenAI’s GPT-4o model to answer based on both the image and the question
- Fallback to GPT-4-turbo (text-only) if image analysis fails

---

## 🧠 LLMs Used and Why

| Model         | Type                | Why Used                        |
|---------------|---------------------|----------------------------------|
| `gpt-4o`      | Multimodal (Vision + Language) | Can understand both images and text, making it perfect for visual QA tasks. |
| `gpt-4-turbo` | Text-only           | Used as a fallback when the image input fails or API returns an error. Ensures robustness. |

OpenAI GPT-4o was chosen for its:
- Native support for **image and text inputs**
- High accuracy and reasoning capabilities
- Simple API interface

---

## 🛠️ Setup Instructions

1. **Install dependencies**:

```bash
pip install openai pillow
Set your OpenAI API key:

In app.py, replace:


client = OpenAI(api_key="your-api-key-here")
with your actual API key. and uncomment that line

Run the app:


python app.py
📊 Test Report: Sample Inputs and Outputs
Test	Image	Question	Response
1️⃣	🖼️ Image of a cat on a bed	"What is the animal doing?"	"The cat is lying down on the bed, possibly resting or sleeping."
2️⃣	🧾 A handwritten math problem (2x + 4 = 10)	"What is the value of x?"	"x = 3"
3️⃣	📊 A bar chart comparing 2022 vs 2023 sales	"Which year had higher sales?"	"2023 had higher sales in most categories according to the chart."

These tests demonstrate the model’s ability to:

Understand general visual content (Test 1)

Read and solve handwritten text (Test 2)

Analyze data visualizations (Test 3)

📦 Folder Structure

Multimodal-QA-Agent/
├── app.py           # Main application file
└── README.md        # Project documentation