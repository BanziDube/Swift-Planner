import tkinter as tk
from tkinter import messagebox
from db import insert_user_data  # Import the function from db.py
from PIL import Image, ImageTk  # Import Image and ImageTk from PIL


def show_register(app, users):
    from login import show_login

    for widget in app.winfo_children():
        widget.destroy()

    app_width = 1600
    app_height = 1600
    app.geometry(f"{app_width}x{app_height}")

    # Load and set background image
    try:
        bg = Image.open("bg.jpg").resize((app_width, app_height))
        bg_img = ImageTk.PhotoImage(bg)
    except FileNotFoundError:
        print("❌ bg.jpg not found.")
        bg_img = None

    canvas = tk.Canvas(app, width=app_width,
                       height=app_height, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    if bg_img:
        canvas.create_image(0, 0, image=bg_img, anchor="nw")
        canvas.image = bg_img  # Keep reference

    # Registration container
    container = tk.Frame(app, bg="#ffffff")
    container.place(relx=0.5, rely=0.5, anchor="center", width=400, height=400)

    tk.Label(container, text="Swift Planner", font=("Helvetica", 20,
             "bold"), fg="#000000", bg="white").pack(pady=(20, 10))

    # Name
    tk.Label(container, text="Name", font=("Arial", 12),
             fg="#333", bg="white").pack(pady=(5, 0))
    entry_name = tk.Entry(container, font=("Arial", 12),
                          width=30, bd=1, relief="solid")
    entry_name.pack(pady=(0, 10))

    # Email
    tk.Label(container, text="Email", font=("Arial", 12),
             fg="#333", bg="white").pack(pady=(5, 0))
    entry_email = tk.Entry(container, font=("Arial", 12),
                           width=30, bd=1, relief="solid")
    entry_email.pack(pady=(0, 10))

    # Password with toggle
    tk.Label(container, text="Password", font=("Arial", 12),
             fg="#333", bg="white").pack(pady=(5, 0))
    password_frame = tk.Frame(container, bg="white")
    password_frame.pack(pady=(0, 10))

    entry_password = tk.Entry(password_frame, show="*",
                              font=("Arial", 12), width=24, bd=1, relief="solid")
    entry_password.pack(side="left")

    show_password = False

    def toggle_password():
        nonlocal show_password
        show_password = not show_password
        entry_password.config(show="" if show_password else "*")
        toggle_btn.config(text="🙈" if show_password else "👁")

    toggle_btn = tk.Button(password_frame, text="👁",
                           command=toggle_password, bg="white", bd=0)
    toggle_btn.pack(side="left", padx=5)

    # Confirm Password with toggle
    tk.Label(container, text="Confirm Password", font=(
        "Arial", 12), fg="#333", bg="white").pack(pady=(5, 0))
    confirm_frame = tk.Frame(container, bg="white")
    confirm_frame.pack(pady=(0, 20))

    entry_confirm = tk.Entry(confirm_frame, show="*",
                             font=("Arial", 12), width=24, bd=1, relief="solid")
    entry_confirm.pack(side="left")

    show_confirm = False

    def toggle_confirm():
        nonlocal show_confirm
        show_confirm = not show_confirm
        entry_confirm.config(show="" if show_confirm else "*")
        toggle_confirm_btn.config(text="🙈" if show_confirm else "👁")

    toggle_confirm_btn = tk.Button(
        confirm_frame, text="👁", command=toggle_confirm, bg="white", bd=0)
    toggle_confirm_btn.pack(side="left", padx=5)

    # Registration logic
    def register_user():
        name = entry_name.get()
        email = entry_email.get()
        password = entry_password.get()
        confirm_password = entry_confirm.get()

        if not name or not email or not password or not confirm_password:
            messagebox.showerror("Error", "All fields are required.")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        try:
            # Attempt to store the data in Firebase
            insert_user_data(name, email, password)
            messagebox.showinfo("Success", "Registration successful!")
            show_login(app, users)

        except Exception as e:
            messagebox.showerror("Error", f"Registration failed.\n{e}")
        insert_user_data(name, email, password)
        messagebox.showinfo("Success", "Registration successful!")
        show_login(app, users)

    # Buttons
    tk.Button(container, text="Register", command=register_user, bg="#1565C0",
              fg="white", font=("Arial", 8, "bold"), width=10).pack(pady=5)
    tk.Button(container, text="Back to Login", command=lambda: show_login(
        app, users), bg="#64B5F6", fg="white", font=("Arial", 8, "bold"), width=10).pack(pady=5)
