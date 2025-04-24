import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

# List of image paths and their overlay texts
IMAGES = [
    ("images/wedding.png", "Weddings"),
    ("images/conference.png", "Conferences"),
    ("images/birthday.png", "Birthdays"),
    ("images/launch.png", "Product Launches"),
    ("images/babyshower.png", "Baby Showers")
]


class LandingPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="white")

        # Navbar
        navbar = tk.Frame(self, bg="#333", height=50)
        navbar.pack(fill="x")
        logo = tk.Label(navbar, text="Swift Planner", fg="white",
                        bg="#333", font=("Arial", 16, "bold"))
        logo.pack(side="left", padx=20)

        signup_btn = tk.Button(
            navbar, text="Sign Up", command=self.controller.show_signup, bg="#555", fg="white")
        signin_btn = tk.Button(
            navbar, text="Sign In", command=self.controller.show_login, bg="#555", fg="white")
        signin_btn.pack(side="right", padx=10, pady=10)
        signup_btn.pack(side="right", pady=10)

        # Slideshow area
        self.slide_index = 0
        self.slideshow_frame = tk.Frame(
            self, width=600, height=300, bg="black")
        self.slideshow_frame.pack(pady=10)
        self.image_label = tk.Label(self.slideshow_frame)
        self.image_label.pack()
        self.overlay_text = tk.Label(self.slideshow_frame, text="", font=(
            "Arial", 20, "bold"), fg="white", bg="black")
        self.overlay_text.place(relx=0.5, rely=0.9, anchor="center")

        # Welcome Text
        self.title = tk.Label(self, text="Plan your events effortlessly with Swift Planner",
                              font=("Helvetica", 16), bg="white")
        self.title.pack(pady=10)
        self.subtitle = tk.Label(
            self, text="Smarter | Simpler | Smoother", font=("Arial", 12), bg="white")
        self.subtitle.pack(pady=5)

        # Footer (Socials + Contact)
        footer = tk.Frame(self, bg="#f0f0f0")
        footer.pack(fill="x", side="bottom", pady=10)

        contact_label = tk.Label(
            footer, text="Contact Us: support@swiftplanner.com", bg="#f0f0f0")
        contact_label.pack(pady=5)

        socials = tk.Frame(footer, bg="#f0f0f0")
        socials.pack()
        for icon in ["facebook", "instagram", "twitter"]:
            try:
                img = Image.open(f"images/{icon}-icon.png")
                img = img.resize((24, 24))
                img = ImageTk.PhotoImage(img)
                label = tk.Label(socials, image=img, bg="#f0f0f0")
                label.image = img  # Keep reference
                label.pack(side="left", padx=5)
            except:
                pass

        self.show_slide()

    def show_slide(self):
        img_path, text = IMAGES[self.slide_index]
        try:
            image = Image.open(img_path)
            image = image.resize((600, 300))
            photo = ImageTk.PhotoImage(image)
            self.image_label.configure(image=photo)
            self.image_label.image = photo
            self.overlay_text.config(text=text)
        except:
            self.overlay_text.config(text="Image not found")

        self.slide_index = (self.slide_index + 1) % len(IMAGES)
        self.after(4000, self.show_slide)

# Controller stub for navigation


def show_landing():
    root = tk.Tk()
    root.title("Swift Planner - Landing")
    root.geometry("700x600")

    class DummyController:
        def show_signup(self):
            print("Go to Signup")

        def show_login(self):
            print("Go to Login")

    app = LandingPage(root, DummyController())
    app.pack(fill="both", expand=True)
    root.mainloop()


if __name__ == '__main__':
    show_landing()
