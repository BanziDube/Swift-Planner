import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def show_login(app, users):
    from register import show_register

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

    canvas = tk.Canvas(app, width=app_width, height=app_height, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    if bg_img:
        canvas.create_image(0, 0, image=bg_img, anchor="nw")
        canvas.image = bg_img  # Keep reference to avoid garbage collection

    # Login container (on top)
    container = tk.Frame(app, bg="#ffffff")
    container.place(relx=0.5, rely=0.5, anchor="center", width=400, height=400)

    # Title
    tk.Label(container, text="Swift Planner", font=("Helvetica", 20, "bold"), fg="#000000", bg="white").pack(pady=(20, 10))

    # Email input with icon
    tk.Label(container, text="Email", font=("Arial", 12), fg="#333", bg="white").pack(pady=(10, 0))
    email_frame = tk.Frame(container, bg="white")
    email_frame.pack(pady=(0, 10))

    entry_email = tk.Entry(email_frame, font=("Arial", 12), width=28, bd=1, relief="solid")
    entry_email.pack(side="left")

    email_icon = tk.Label(email_frame, text="📧", bg="white", font=("Arial", 12))
    email_icon.pack(side="left", padx=5)

    # Password input with toggle
    tk.Label(container, text="Password", font=("Arial", 12), fg="#333", bg="white").pack(pady=(10, 0))
    password_frame = tk.Frame(container, bg="white")
    password_frame.pack(pady=(0, 10))

    entry_password = tk.Entry(password_frame, show="*", font=("Arial", 12), width=28, bd=1, relief="solid")
    entry_password.pack(side="left")

    show_password = False

    def toggle_password():
        nonlocal show_password
        show_password = not show_password
        entry_password.config(show="" if show_password else "*")
        toggle_btn.config(text="🙈" if show_password else "👁")

    toggle_btn = tk.Button(password_frame, text="👁", command=toggle_password, bg="white", bd=0)
    toggle_btn.pack(side="left", padx=5)

    # Login function
    def login_user():
        email = entry_email.get()
        password = entry_password.get()
        user = users.get(email)
        if user and user["password"] == password:
            messagebox.showinfo("Login Successful", f"Welcome {user['name']}!")
        else:
            messagebox.showerror("Login Failed", "Invalid email or password.")

    # Buttons
    tk.Button(container, text="Login", command=login_user, bg="#1565C0", fg="white",
              font=("Arial", 8, "bold"), width=10).pack(pady=5)

    tk.Button(container, text="Register", command=lambda: show_register(app, users), bg="#64B5F6", fg="white",
              font=("Arial", 8, "bold"), width=10).pack(pady=5)
