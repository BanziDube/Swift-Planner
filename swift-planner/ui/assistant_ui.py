# ui/assistant_ui.py

import tkinter as tk
from utils.ai_assistant import get_ai_response


def show_assistant_ui(root):
    window = tk.Toplevel(root)
    window.title("Swift Assistant")
    window.geometry("400x300")

    chat_display = tk.Text(window, wrap=tk.WORD, height=15, state='disabled')
    chat_display.pack(padx=10, pady=10)

    entry = tk.Entry(window, width=40)
    entry.pack(padx=10, pady=5)

    def send_message():
        user_message = entry.get()
        if user_message:
            entry.delete(0, tk.END)
            response = get_ai_response(user_message)

            chat_display.config(state='normal')
            chat_display.insert(tk.END, f"You: {user_message}\n")
            chat_display.insert(tk.END, f"Assistant: {response}\n\n")
            chat_display.config(state='disabled')
            chat_display.see(tk.END)

    send_button = tk.Button(window, text="Ask", command=send_message)
    send_button.pack(pady=5)
