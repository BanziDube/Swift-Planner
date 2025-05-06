import tkinter as tk
from PIL import Image, ImageTk, ImageOps
# Replace this with your real function
from landing_page import show_landing_page


def show_landing():
    splash.destroy()
    app = tk.Tk()
    app.title("Swift Planner")
    app.state('zoomed')  # This makes the main window fullscreen
    show_landing_page(app)
    app.mainloop()


# Create splash screen window
splash = tk.Tk()
splash.title("Splash Screen")

# Get screen size
screen_width = splash.winfo_screenwidth()
screen_height = splash.winfo_screenheight()

# Set splash window size and position
splash.geometry(f"{screen_width}x{screen_height}+0+0")

# Load and resize image
try:
    image = Image.open("splash_image.png")
    image = image.resize((screen_width, screen_height),
                         Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(splash, image=photo)
    label.image = photo
    label.pack()
except Exception as e:
    print(f"Error loading splash image: {e}")

# Show landing page after 5 seconds
splash.after(5000, show_landing)
splash.mainloop()
