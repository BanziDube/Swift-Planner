# ui/main_menu.py

import tkinter as tk
from ui.assistant_ui import show_assistant_ui


def show_main_menu(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Welcome to Swift Planner",
             font=("Helvetica", 16)).pack(pady=20)

    tk.Button(root, text="Create Event", width=20).pack(pady=10)
    tk.Button(root, text="View My Events", width=20).pack(pady=10)
    tk.Button(root, text="Logout", width=20).pack(pady=10)
    tk.Button(root, text="Ask Swift Assistant",
              command=lambda: show_assistant_ui(root)).pack(pady=10)
