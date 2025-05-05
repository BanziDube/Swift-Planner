import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # FIX: Correct placement of imports
from firebase_config import auth, db  # Firebase Auth and Firestore
import login  # FIX: Prevent circular import issue
import bcrypt  # For hashing passwords
from tkinter import ttk  # FIX: Placed import at the top for consistency


def show_register(app, users):
    """Function to display the registration screen."""

    for widget in app.winfo_children():
        widget.destroy()

    app.geometry("500x600")
    app.configure(bg="#f0f0f0")
    app.resizable(True, True)

    # Create a menu bar
    menu_bar = tk.Frame(app, bg="#6f42c1", height=50)
    menu_bar.pack(fill="x", side="top")

    # Load and display the logo (FIXED)
    try:
        logo_image = Image.open("swift.png")  # Load image properly
        logo_image = logo_image.resize((200, 60))  # Resize using PIL
        logo = ImageTk.PhotoImage(logo_image)  # Convert for Tkinter
        logo_label = tk.Label(menu_bar, image=logo, bg="#6f42c1")
        logo_label.image = logo  # Prevent garbage collection
        logo_label.pack(side="left", padx=10, pady=5)
    except Exception as e:
        print(f"Error loading image: {e}")

    # Create a burger menu button
    burger_menu = tk.Button(menu_bar, text="☰", font=(
        "Arial", 16), bg="#6f42c1", fg="white", bd=0)
    burger_menu.pack(side="right", padx=10)

    # Dropdown menu functionality
    def toggle_menu():
        popup = tk.Menu(app, tearoff=0)
        popup.add_command(label="Home")
        popup.add_command(label="Settings")
        popup.add_command(label="Logout")
        try:
            popup.tk_popup(burger_menu.winfo_rootx(
            ), burger_menu.winfo_rooty() + burger_menu.winfo_height())
        finally:
            popup.grab_release()

    burger_menu.config(command=toggle_menu)

    # Heading section
    heading_frame = tk.Frame(app, bg="#f0f0f0")
    heading_frame.pack(pady=(40, 10))

    # tk.Label(heading_frame, text="Register Account", font=("Helvetica", 24, "bold"), fg="black", bg="#f0f0f0").pack()

    # Registration container
    container = tk.Frame(app, bg="#ffffff", bd=2, relief="groove")
    container.place(relx=0.5, rely=0.55, anchor="center",
                    width=400, height=460)

    tk.Label(container, text="Register Account", font=(
        "Helvetica", 20, "bold"), fg="#000000", bg="white").pack(pady=(20, 10))

    # Create a custom style for rounded entries
    style = ttk.Style()
    style.configure("Rounded.TEntry",
                    borderwidth=10,
                    relief="solid",
                    padding=5)

    # Username Input (Rounded)
    tk.Label(container, text="Username", font=("Arial", 12), fg="#333",
             bg="white", anchor="w").pack(fill="x", padx=20, pady=(5, 0))
    entry_name = ttk.Entry(container, font=("Arial", 12),
                           width=30, style="Rounded.TEntry")
    entry_name.pack(fill="x", padx=20, pady=(0, 10))

    # Email Input (Rounded)
    tk.Label(container, text="Email", font=("Arial", 12), fg="#333",
             bg="white", anchor="w").pack(fill="x", padx=20, pady=(5, 0))
    entry_email = ttk.Entry(container, font=(
        "Arial", 12), width=30, style="Rounded.TEntry")
    entry_email.pack(fill="x", padx=20, pady=(0, 10))

    # Password Input (Rounded)
    tk.Label(container, text="Password", font=("Arial", 12), fg="#333",
             bg="white", anchor="w").pack(fill="x", padx=20, pady=(5, 0))
    password_frame = tk.Frame(container, bg="white")
    password_frame.pack(fill="x", padx=20, pady=(0, 10))

    entry_password = ttk.Entry(
        password_frame, show="*", font=("Arial", 12), width=30, style="Rounded.TEntry")
    entry_password.pack(side="left", expand=True, fill="x")

    def toggle_password():
        entry_password.config(
            show="" if entry_password.cget("show") == "*" else "*")

    tk.Button(password_frame, text="👁", command=toggle_password,
              bg="white", bd=0).pack(side="right", padx=5)

    # Confirm Password Input (Rounded)
    tk.Label(container, text="Confirm Password", font=("Arial", 12),
             fg="#333", bg="white", anchor="w").pack(fill="x", padx=20, pady=(5, 0))
    confirm_frame = tk.Frame(container, bg="white")
    confirm_frame.pack(fill="x", padx=20, pady=(0, 10))

    entry_confirm = ttk.Entry(
        confirm_frame, show="*", font=("Arial", 12), width=30, style="Rounded.TEntry")
    entry_confirm.pack(side="left", expand=True, fill="x")

    def toggle_confirm():
        entry_confirm.config(
            show="" if entry_confirm.cget("show") == "*" else "*")

    tk.Button(confirm_frame, text="👁", command=toggle_confirm,
              bg="white", bd=0).pack(side="right", padx=5)

    # Registration logic (FIXED)
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
            auth.create_user_with_email_and_password(email, password)

            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(
                password.encode('utf-8'), salt).decode('utf-8')

            user_data = {
                "name": name,
                "email": email,
                "password": hashed_password
            }

            db.collection("users").add(user_data)
            messagebox.showinfo("Success", "Registration successful!")
            login.show_login(app, users)  # FIX: Correct function call

        except Exception as e:
            messagebox.showerror("Error", f"Registration failed.\n{e}")

    # Buttons (UNCHANGED)
    tk.Button(container, text="Register", command=register_user, bg="#1565C0",
              fg="white", font=("Arial", 8, "bold"), width=15).pack(pady=5)

    tk.Button(container, text="Back to Login", command=lambda: login.show_login(app, users),
              bg="#64B5F6", fg="white", font=("Arial", 8, "bold"), width=15).pack(pady=5)
