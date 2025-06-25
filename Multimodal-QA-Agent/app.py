import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import base64
from openai import OpenAI
from io import BytesIO

# Set your OpenAI API key
# client = OpenAI(api_key="your-api-key-here")

def encode_image_to_base64(img_path):
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def call_gpt4o(image_b64, question):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": [
                    {"type": "text", "text": question},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_b64}"}}
                ]}
            ],
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[Error] {str(e)}"

def call_gpt4_text_only(question):
    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": question}],
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[Error - Text Fallback] {str(e)}"

class MultimodalQAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Multimodal QA Agent")

        self.image_path = None

        # UI Components
        self.label = tk.Label(root, text="Upload an Image:")
        self.label.pack()

        self.upload_btn = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_btn.pack()

        self.image_panel = tk.Label(root)
        self.image_panel.pack()

        self.question_entry = tk.Entry(root, width=80)
        self.question_entry.pack(pady=10)
        self.question_entry.insert(0, "Enter your question about the image...")

        self.ask_btn = tk.Button(root, text="Ask", command=self.answer_question)
        self.ask_btn.pack()

        self.response_text = tk.Text(root, height=10, wrap=tk.WORD)
        self.response_text.pack(pady=10)

    def upload_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
        if path:
            self.image_path = path
            img = Image.open(path)
            img.thumbnail((400, 400))
            self.tk_image = ImageTk.PhotoImage(img)
            self.image_panel.config(image=self.tk_image)

    def answer_question(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please upload an image.")
            return

        question = self.question_entry.get()
        if not question.strip():
            messagebox.showerror("Error", "Please enter a question.")
            return

        self.response_text.delete(1.0, tk.END)
        self.response_text.insert(tk.END, "Thinking...\n")

        image_b64 = encode_image_to_base64(self.image_path)
        answer = call_gpt4o(image_b64, question)

        if answer.startswith("[Error]"):
            fallback = call_gpt4_text_only(question)
            answer += "\n\n[Fallback to text-only model]\n" + fallback

        self.response_text.delete(1.0, tk.END)
        self.response_text.insert(tk.END, answer)

if __name__ == "__main__":
    root = tk.Tk()
    app = MultimodalQAApp(root)
    root.mainloop()
