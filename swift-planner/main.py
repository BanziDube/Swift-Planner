# main.py
import tkinter as tk
from ui.login_ui import show_login_screen
from utils.db import create_tables  # ✅ Import create_tables
from ui.login_ui import show_login_screen


def main():
    create_tables()  # ✅ Make sure tables exist before anything else

    root = tk.Tk()
    root.title("Swift Planner")
    root.geometry("500x400")

    show_login_screen(root)

    root.mainloop()


if __name__ == "__main__":
    main()
