import tkinter as tk
from login import show_login
from event_ui import EventPlannerApp  # Import the event UI function


# Global user storage (simulating a database)
users = {}

app = tk.Tk()
app.title("Login System")
app.geometry("300x250")

# Show login page and pass app + users dict
show_login(app, users)

app.mainloop()
