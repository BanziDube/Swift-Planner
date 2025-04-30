import tkinter as tk
from landing_page import show_landing_page
from register import show_register
from login import show_login

# Store registered users in memory (you could use a database later)
users = {}

# Set up main app window
root = tk.Tk()
root.title("Swift Planner")

# Make the window resizable
root.resizable(True, True)

# Start in fullscreen
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")

# Allow fullscreen toggle


def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))


root.bind("<F11>", toggle_fullscreen)  # Press F11 to toggle fullscreen
root.bind("<Escape>", lambda e: root.attributes(
    "-fullscreen", False))  # Escape key exits fullscreen

# Landing Page with button handlers


def open_register():
    show_register(root, users)


def open_login():
    show_login(root, users)


# Load landing page dynamically
show_landing_page(root, on_signup=open_register, on_signin=open_login)

# Start the GUI loop
root.mainloop()
