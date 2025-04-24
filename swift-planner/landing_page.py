# landing_page.py
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os


def show_landing_page(root, on_signup=None, on_signin=None):
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="white")

    navbar = tk.Frame(root, bg="black", height=50)
    navbar.pack(fill="x", side="top")

    logo = tk.Label(navbar, text="Swift Planner", bg="black", fg="white",
                    font=("Times New Roman", 20, "bold"))
    logo.pack(side="left", padx=20, pady=10)

    nav_buttons = tk.Frame(navbar, bg="black")
    nav_buttons.pack(side="right", padx=20)

    signup_btn = tk.Button(nav_buttons, text="Sign Up",
                           font=("Arial", 12), bg="red", fg="black", borderwidth=5, command=on_signup)
    signup_btn.pack(side="left", padx=10)

    signin_btn = tk.Button(nav_buttons, text="Sign In",
                           font=("Arial", 12), bg="red", fg="black",  borderwidth=5, command=on_signin)
    signin_btn.pack(side="left")

    heading_label = tk.Label(
        root,
        text="Welcome to Swift Planner, where event planning is made simple.",
        font=("Helvetica", 22, "bold"),
        fg="black",
        bg="white",
    )
    heading_label.pack(pady=(20, 10))

    # Slideshow Frame
    slideshow_frame = tk.Frame(root, bg="white")
    slideshow_frame.pack(pady=20)

    image_paths = [
        ("images/wedding.png", "Weddings"),
        ("images/conference.png", "Conferences"),
        ("images/birthday.png", "Birthdays"),
        ("images/launch.png", "Product Launches"),
        ("images/babyshower.png", "Baby Showers")
    ]

    slide_label = tk.Label(slideshow_frame)
    slide_label.pack()

    def update_slideshow(index=0):
        path, caption = image_paths[index]
        img = Image.open(path)
        img = img.resize((1300, 350), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)

        slide_label.config(image=photo)
        slide_label.image = photo

        root.after(4000, lambda: update_slideshow(
            (index + 1) % len(image_paths)))

    update_slideshow()

    # Section: Summary + Contact
    summary_contact_container = tk.Frame(root, bg="white")
    summary_contact_container.pack(padx=20, pady=30, fill="both")

    # Summary (Left side)
    summary_frame = tk.Frame(summary_contact_container, bg="white")
    summary_frame.pack(side="left", padx=10, expand=True, fill="both")

    summary_label = tk.Label(summary_frame, text="Why Choose Swift Planner?", font=(
        "Arial", 18, "bold"), fg="black", bg="white", anchor="w", justify="left")
    summary_label.pack(anchor="w")

    summary_text = """Swift Planner helps you plan and manage events with ease.
From weddings and conferences to birthday parties and launches, 
Swift Planner ensures a smooth and stress-free planning experience."""
    summary_message = tk.Label(summary_frame, text=summary_text, font=(
        "Arial", 12), fg="black", bg="white", justify="left", anchor="w")
    summary_message.pack(anchor="w", pady=10)

    # Contact Form (Right side)
    contact_frame = tk.LabelFrame(summary_contact_container, text="Contact Us", font=(
        "Arial", 14, "bold"), bg="white")
    contact_frame.pack(side="right", padx=10, fill="y")

    name_entry = ttk.Entry(contact_frame, width=30)
    email_entry = ttk.Entry(contact_frame, width=30)
    message_entry = tk.Text(contact_frame, height=4, width=30)

    ttk.Label(contact_frame, text="Name:", background="white").grid(
        row=0, column=0, sticky="w", pady=5, padx=5)
    name_entry.grid(row=0, column=1, pady=5, padx=5)

    ttk.Label(contact_frame, text="Email:", background="white").grid(
        row=1, column=0, sticky="w", pady=5, padx=5)
    email_entry.grid(row=1, column=1, pady=5, padx=5)

    ttk.Label(contact_frame, text="Message:", background="white").grid(
        row=2, column=0, sticky="nw", pady=5, padx=5)
    message_entry.grid(row=2, column=1, pady=5, padx=5)

    send_btn = ttk.Button(contact_frame, text="Send")
    send_btn.grid(row=3, column=1, sticky="e", pady=10, padx=5)

    # Footer
    footer = tk.Label(root, text="© 2025 Swift Planner | All rights reserved.", font=(
        "Arial", 10), fg="gray", bg="white")
    footer.pack(pady=10)
