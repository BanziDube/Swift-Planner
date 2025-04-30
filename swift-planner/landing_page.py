import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def show_landing_page(root, on_signup=None, on_signin=None):
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="white")

    # Make window responsive
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Create a scrollable canvas
    canvas = tk.Canvas(root, bg="white")
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)

    scroll_frame = tk.Frame(canvas, bg="white")
    scroll_frame.bind("<Configure>", lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Define custom button style for rounded corners
    style = ttk.Style()
    style.configure("RoundedButton.TButton",
                    background="#be2ed6",
                    foreground="black",
                    padding=6,
                    relief="flat")

    # Navbar (Full width, dynamic resizing)
    navbar = tk.Frame(scroll_frame, bg="#222831", height=60)
    navbar.pack(fill="x", expand=True)

    logo = tk.Label(navbar, text="Swift Planner", bg="#222831", fg="white",
                    font=("Helvetica", 22, "bold"))
    logo.pack(side="left", padx=20, pady=10)

    nav_buttons = tk.Frame(navbar, bg="#222831")
    nav_buttons.pack(side="right", padx=20)

    signup_btn = ttk.Button(nav_buttons, text="Sign Up",
                            style="RoundedButton.TButton", command=on_signup)
    signup_btn.pack(side="left", padx=10)

    signin_btn = ttk.Button(nav_buttons, text="Sign In",
                            style="RoundedButton.TButton", command=on_signin)
    # Adjusted padding for better spacing
    signin_btn.pack(side="left", padx=30)

    # Hero Section with Full-Width Slideshow
    hero_section = tk.Frame(scroll_frame, bg="white")
    hero_section.pack(fill="x", pady=20, expand=True)

    heading_label = tk.Label(hero_section, text="Plan Your Events Effortlessly with Swift Planner",
                             font=("Helvetica", 26, "bold"), fg="black", bg="white")
    heading_label.pack(pady=(10, 20))

    # Slideshow Frame (Responsive size adjustment)
    slideshow_frame = tk.Frame(hero_section, bg="#393E46")
    slideshow_frame.pack(fill="x", expand=True)

    image_paths = [
        ("images/wedding.png", "Weddings"),
        ("images/conference.png", "Conferences"),
        ("images/birthday.png", "Birthdays"),
        ("images/launch.png", "Product Launches"),
        ("images/babyshower.png", "Baby Showers")
    ]

    slide_label = tk.Label(slideshow_frame)
    slide_label.pack(fill="x", expand=True)

    def update_slideshow(index=0):
        path, caption = image_paths[index]
        img = Image.open(path)
        img = img.resize((root.winfo_width(), 400), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)

        slide_label.config(image=photo)
        slide_label.image = photo

        root.after(4000, lambda: update_slideshow(
            (index + 1) % len(image_paths)))

    update_slideshow()

    # Features Section (Fully responsive, updated design)
    features_section = tk.Frame(scroll_frame, bg="#001F3F", padx=20,
                                pady=30, highlightbackground="purple", highlightthickness=3)
    features_section.pack(fill="x", expand=True)

    tk.Label(features_section, text="Why Choose Swift Planner?", font=("Arial", 20, "bold"),
             fg="white", bg="#001F3F").pack(pady=10)  # Centered heading

    features_text = """✓ AI Assistant (SIA) for Smart Event Planning
✓ Venue Suggestions Based on Your Preferences
✓ Budget Estimations to Keep Your Event Organized
✓ Personalized Event Recommendations"""

    features_label = tk.Label(features_section, text=features_text, font=("Arial", 14),
                              fg="white", bg="#001F3F", anchor="w", justify="left")
    features_label.pack(anchor="w", pady=10)

    # Footer (Full width and responsive)
    footer = tk.Label(scroll_frame, text="© 2025 Swift Planner | All rights reserved.",
                      font=("Arial", 10), fg="gray", bg="#222831")
    footer.pack(fill="x", pady=10, expand=True)
