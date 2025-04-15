# ui/login_ui.py

import tkinter as tk
import sqlite3
from ui.main_menu import show_main_menu
import bcrypt  # type: ignore
from utils.db import connect
from tkinter import messagebox


def register_user(username, email, password):
    conn = connect()
    cursor = conn.cursor()

    # Hash and decode password before saving
    hashed_pw = bcrypt.hashpw(password.encode(
        'utf-8'), bcrypt.gensalt()).decode('utf-8')

    try:
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            (username, email, hashed_pw)
        )
        conn.commit()
        messagebox.showinfo("Success", "User registered successfully!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Email already exists.")
    conn.close()


def login_user(email, password, root):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email=?", (email,))
    user = cursor.fetchone()
    conn.close()

    if user and bcrypt.checkpw(password.encode('utf-8'), user[3]):
        messagebox.showinfo("Login Success", f"Welcome {user[1]}!")
        show_main_menu(root)
    else:
        messagebox.showerror("Login Failed", "Invalid credentials.")


def show_login_screen(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Swift Planner Login",
             font=("Helvetica", 14)).pack(pady=10)

    tk.Label(root, text="Email").pack()
    email_entry = tk.Entry(root)
    email_entry.pack()

    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    def handle_login():
        login_user(email_entry.get(), password_entry.get(), root)

    def show_register():
        show_register_screen(root)

    tk.Button(root, text="Login", command=handle_login).pack(pady=5)
    tk.Button(root, text="Register", command=show_register).pack(pady=5)


def show_register_screen(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Register", font=("Helvetica", 14)).pack(pady=10)

    tk.Label(root, text="Username").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Email").pack()
    email_entry = tk.Entry(root)
    email_entry.pack()

    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    def handle_register():
        register_user(username_entry.get(),
                      email_entry.get(), password_entry.get())

    tk.Button(root, text="Submit", command=handle_register).pack(pady=5)
    tk.Button(root, text="Back to Login",
              command=lambda: show_login_screen(root)).pack()
