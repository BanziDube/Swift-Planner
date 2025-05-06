import tkinter as tk
from tkinter import messagebox
import pyrebase
from PIL import Image, ImageTk
import register  # Import whole module to prevent circular import issues
# Assuming this is your event planner app
from event_ui import EventPlannerApp

# Firebase Configuration
firebase_config = {
    "apiKey": "AIzaSyBuXq6tiEWaceoTsPwKhdy_pIYsd5FzdpY",
    "authDomain": "swift-planner.firebaseapp.com",
    "databaseURL": "https://console.firebase.google.com/u/1/project/swift-planner/settings/general/web:N2EwNWZmOGYtNzA1OS00ODI4LWFhYjgtNDViM2RmMGFkMGZm",  # ✅ Important
    "projectId": "swift-planner",
    "storageBucket": "swift-planner.appspot.com",  # ✅ Corrected
    "messagingSenderId": "200233391727",
    "appId": "1:200233391727:web:0036940cf9e08c7d591f9a"
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()


def show_login(app, users):
    """Function to display the login screen."""

    for widget in app.winfo_children():
        widget.destroy()

    app.geometry("500x600")
    app.configure(bg="#f0f0f0")
    app.resizable(True, True)

    # Create a menu bar
    menu_bar = tk.Frame(app, bg="#6f42c1", height=50)
    menu_bar.pack(fill="x", side="top")

    # Load and display the logo
    try:
        logo_image = Image.open("swift.png")
        logo_image = logo_image.resize((200, 60))
        logo = ImageTk.PhotoImage(logo_image)
        logo_label = tk.Label(menu_bar, image=logo, bg="#6f42c1")
        logo_label.image = logo  # Keep reference
        logo_label.pack(side="left", padx=10, pady=5)
    except Exception as e:
        print(f"Error loading image: {e}")

    # Burger menu
    burger_menu = tk.Button(menu_bar, text="☰", font=(
        "Arial", 16), bg="#6f42c1", fg="white", bd=0)
    burger_menu.pack(side="right", padx=10)

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

    # Headings
    heading_frame = tk.Frame(app, bg="#f0f0f0")
    heading_frame.pack(pady=(40, 10))
    tk.Label(heading_frame, text="Sign into your account", font=(
        "Helvetica", 24, "bold"), fg="black", bg="#f0f0f0").pack()
    tk.Label(heading_frame, text="Plan your next perfect event",
             font=("Helvetica", 16), fg="gray", bg="#f0f0f0").pack()

    # Login Container
    container = tk.Frame(app, bg="#ffffff", bd=2, relief="groove")
    container.place(relx=0.5, rely=0.55, anchor="center",
                    width=400, height=350)

    # Email Entry
    tk.Label(container, text="Email address", font=("Arial", 12), fg="#333",
             bg="white", anchor="w").pack(fill="x", padx=20, pady=(10, 0))
    email_frame = tk.Frame(container, bg="white")
    email_frame.pack(fill="x", padx=20, pady=(0, 10))
    entry_email = tk.Entry(email_frame, font=(
        "Arial", 12), width=30, bd=1, relief="solid")
    entry_email.pack(side="left", expand=True, fill="x")

    # Password Entry
    tk.Label(container, text="Password", font=("Arial", 12), fg="#333",
             bg="white", anchor="w").pack(fill="x", padx=20, pady=(10, 0))
    password_frame = tk.Frame(container, bg="white")
    password_frame.pack(fill="x", padx=20, pady=(0, 10))
    entry_password = tk.Entry(password_frame, show="*",
                              font=("Arial", 12), width=30, bd=1, relief="solid")
    entry_password.pack(side="left", expand=True, fill="x")

    # Remember Me
    options_frame = tk.Frame(container, bg="white")
    options_frame.pack(fill="x", padx=20, pady=(5, 10))
    remember_me = tk.Checkbutton(
        options_frame, text="Remember me", bg="white", font=("Arial", 10))
    remember_me.pack(side="left")
    tk.Label(options_frame, text="Forgot your password?", fg="blue", bg="white", font=(
        "Arial", 10, "underline"), cursor="hand2").pack(side="right")

    # Firebase login logic
    def handle_login():
        email = entry_email.get()
        password = entry_password.get()

        if not email or not password:
            messagebox.showerror("Error", "Both fields are required.")
            return

        try:
            user = auth.sign_in_with_email_and_password(email, password)
            messagebox.showinfo("Login Successful", f"Welcome, {email}!")
            for widget in app.winfo_children():
                widget.destroy()
            EventPlannerApp(app)  # Replace with your app function
        except Exception as e:
            error_message = str(e)
            messagebox.showerror(
                "Login Failed", "Invalid credentials. Please try again.")
            print("Login error:", error_message)

    # Login Button
    tk.Button(container, text="Sign in", bg="#1565C0", fg="white", font=("Arial", 12, "bold"),
              width=25, command=handle_login).pack(pady=15)

    # Social login UI (non-functional placeholders)
    tk.Label(container, text="Or continue with", font=(
        "Arial", 12), fg="gray", bg="white").pack(pady=(10, 5))
    social_frame = tk.Frame(container, bg="white")
    social_frame.pack()
    tk.Button(social_frame, text="Google", bg="#db4437", fg="white", font=(
        "Arial", 10, "bold"), width=12).pack(side="left", padx=10)
    tk.Button(social_frame, text="Other", bg="#4285F4", fg="white",
              font=("Arial", 10, "bold"), width=12).pack(side="left")

    # Register Link
    register_label = tk.Label(container, text="Not registered? Create an account", fg="blue", bg="white",
                              font=("Arial", 10, "underline"), cursor="hand2")

    def go_to_register(event):
        register.show_register(app, users)

    register_label.bind("<Button-1>", go_to_register)
    register_label.pack(pady=10)
