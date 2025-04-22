import tkinter as tk
from landing_page import show_landing_page
from register import show_register
from login import show_login

# Store registered users in memory (you could use a database later)
users = {}

# Set up main app window
root = tk.Tk()
root.title("Swift Planner")
root.geometry("1300x800")
root.resizable(False, False)

# Landing Page with button handlers


def open_register():
    show_register(root, users)


def open_login():
    show_login(root, users)


# Load landing page
show_landing_page(root, on_signup=open_register, on_signin=open_login)

# Start the GUI loop
root.mainloop()
