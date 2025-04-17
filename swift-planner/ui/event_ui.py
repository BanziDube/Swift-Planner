import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import uuid
from datetime import datetime
from tkcalendar import DateEntry, Calendar

# -------------------- Event Model -------------------- #
class Event:
    def __init__(self, title, date, time, location, description, budget, owner, priority, event_id=None):
        self.id = event_id or str(uuid.uuid4())
        self.title = title
        self.date = date
        self.time = time
        self.location = location
        self.description = description
        self.budget = budget
        self.owner = owner
        self.priority = priority

# -------------------- Invitation Model -------------------- #
class Invitation:
    def __init__(self, name, surname, email, event_title, owner, date, time, location):
        self.id = str(uuid.uuid4())
        self.name = name
        self.surname = surname
        self.email = email
        self.event_title = event_title
        self.owner = owner
        self.date = date
        self.time = time
        self.location = location

# -------------------- Main App -------------------- #
class EventPlannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎉 Dashboard")
        self.root.geometry("1200x700")
        self.root.configure(bg="#f0f4f8")

        self.events = []
        self.invitations = []
        self.editing_event = None
        self.selected_event_for_invitation = None

        self.build_ui()

    def build_ui(self):
        header = tk.Label(self.root, text="📅 Dashboard", font=("Helvetica", 30, "bold"), fg="#2c3e50", bg="#f0f4f8")
        header.pack(pady=(5, 5))

        subtitle = tk.Label(self.root, text="Plan, manage, and update your events with ease.",
                            font=("Arial", 12), fg="#6c757d", bg="#f0f4f8")
        subtitle.pack(pady=(0, 20))

        sidebar = tk.Frame(self.root, bg="#2c3e50", width=100)
        sidebar.pack(side="left", fill="y")

        self.toggle_button = tk.Button(sidebar, text="📖", font=("Arial", 20), bg="#2c3e50", fg="white",
                                       bd=0, activebackground="#34495e", command=self.toggle_main_content)
        self.toggle_button.pack(pady=(30, 10))

        self.calendar_icon_btn = tk.Button(sidebar, text="📅", font=("Arial", 20), bg="#2c3e50", fg="white",
                                           bd=0, activebackground="#34495e", command=self.show_calendar_with_highlighted_dates)
        self.calendar_icon_btn.pack(pady=(0, 10))

        self.invitation_icon_btn = tk.Button(sidebar, text="📩", font=("Arial", 20), bg="#2c3e50", fg="white",
                                             bd=0, activebackground="#34495e", command=self.open_invitation_form)
        self.invitation_icon_btn.pack(pady=(0, 30))

        sidebar_bottom = tk.Frame(sidebar, bg="#2c3e50")
        sidebar_bottom.pack(side="bottom", pady=20)

        help_button = tk.Button(sidebar_bottom, text="💬", font=("Arial", 18), bg="#2c3e50", fg="white",
                                bd=0, activebackground="#34495e", command=self.open_help_popup)
        help_button.pack()

        self.main_content = tk.Frame(self.root, bg="#f0f4f8")
        self.main_content.pack(side="left", fill="both", expand=True)

        content_wrapper = tk.Frame(self.main_content, bg="#f0f4f8")
        content_wrapper.pack(fill="both", expand=True, padx=10, pady=10)

        self.build_form_section(content_wrapper)
        self.build_event_and_invitation_sections(content_wrapper)

        footer = tk.Label(self.root, text="Event Planner © 2025", font=("Arial", 10), fg="white", bg="#2c3e50")
        footer.pack(side="bottom", pady=10)

    def build_form_section(self, parent):
        form_frame = tk.Frame(parent, bg="white", bd=2, relief="ridge", padx=10, pady=10)
        form_frame.pack(side="left", fill="y", padx=(0, 10), pady=10)

        tk.Label(form_frame, text="📝 Create Events", font=("Arial", 14, "bold"), fg="#333", bg="white").pack(pady=(10, 15))

        field_font = ("Arial", 11)
        field_container = tk.Frame(form_frame, bg="white")
        field_container.pack(padx=5, pady=5, anchor="w")

        labels = ["Title:", "Date:", "Time (HH:MM):", "Location:", "Description:", "Budget (R):", "Owner:", "Priority:"]
        self.title_entry = tk.Entry(field_container, width=25, font=field_font)
        self.date_entry = DateEntry(field_container, width=22, font=field_font, date_pattern="yyyy-mm-dd")
        self.time_entry = tk.Entry(field_container, width=25, font=field_font)
        self.location_entry = tk.Entry(field_container, width=25, font=field_font)
        self.description_entry = tk.Entry(field_container, width=25, font=field_font)
        self.budget_entry = tk.Entry(field_container, width=25, font=field_font)
        self.owner_entry = tk.Entry(field_container, width=25, font=field_font)
        self.priority_var = tk.StringVar(value="LOW")
        priority_menu = ttk.Combobox(field_container, textvariable=self.priority_var, values=["LOW", "HIGH"], width=23, font=field_font)

        inputs = [self.title_entry, self.date_entry, self.time_entry, self.location_entry,
                  self.description_entry, self.budget_entry, self.owner_entry, priority_menu]

        for i, label in enumerate(labels):
            tk.Label(field_container, text=label, bg="white", font=field_font).grid(row=i, column=0, sticky="w", pady=4, padx=(0, 10))
            inputs[i].grid(row=i, column=1, pady=4)

        button_frame = tk.Frame(form_frame, bg="white")
        button_frame.pack(pady=(15, 5))

        self.submit_button = tk.Button(button_frame, text="CREATE EVENT", command=self.create_or_update_event,
                                       bg="#007bff", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5)
        self.submit_button.grid(row=0, column=0, padx=5)

        clear_button = tk.Button(button_frame, text="CLEAR FORM", command=self.clear_form,
                                 bg="#6c757d", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5)
        clear_button.grid(row=0, column=1, padx=5)

        cancel_button = tk.Button(button_frame, text="CANCEL EDIT", command=self.cancel_edit,
                                  bg="#dc3545", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5)
        cancel_button.grid(row=0, column=2, padx=5)

    def build_event_and_invitation_sections(self, parent):
        section_wrapper = tk.Frame(parent, bg="#f0f4f8")
        section_wrapper.pack(side="left", fill="both", expand=True)

        event_list_frame = tk.Frame(section_wrapper, bg="white", bd=2, relief="ridge")
        event_list_frame.pack(side="left", fill="both", expand=True, pady=10)

        tk.Label(event_list_frame, text="📋  Events", font=("Arial", 14, "bold"), fg="#333", bg="white").pack(pady=(10, 15))

        self.canvas = tk.Canvas(event_list_frame, bg="white")
        self.scrollbar = tk.Scrollbar(event_list_frame, orient="vertical", command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True, padx=20)
        self.scrollbar.pack(side="right", fill="y")

        self.event_frame = tk.Frame(self.canvas, bg="white")
        self.canvas.create_window((0, 0), window=self.event_frame, anchor="nw")
        self.event_frame.bind("<Configure>", lambda e: self.canvas.config(scrollregion=self.canvas.bbox("all")))

        # Invitations panel
        self.invite_frame = tk.Frame(section_wrapper, bg="white", bd=2, relief="ridge", width=280)
        self.invite_frame.pack(side="right", fill="y", pady=10, padx=(10, 0))
        tk.Label(self.invite_frame, text="📨 Sent Invitations", font=("Arial", 14, "bold"), bg="white", fg="#333").pack(pady=10)

    def open_invitation_form(self):
        if not self.selected_event_for_invitation:
            messagebox.showinfo("No Event", "Please edit/select an event first.")
            return

        event = self.selected_event_for_invitation
        popup = tk.Toplevel(self.root)
        popup.title("📩 Send Invitation")
        popup.geometry("400x400")
        popup.configure(bg="white")

        tk.Label(popup, text="Send Invitation", font=("Arial", 14, "bold"), bg="white").pack(pady=10)

        def label_input(text, default=""):
            tk.Label(popup, text=text, bg="white", anchor="w").pack(pady=(10, 0))
            entry = tk.Entry(popup, width=40)
            entry.insert(0, default)
            entry.pack()
            return entry

        name_entry = label_input("Name:")
        surname_entry = label_input("Surname:")
        email_entry = label_input("Email:")
        title_entry = label_input("Event Title:", event.title)
        owner_entry = label_input("Owner:", event.owner)
        date_entry = label_input("Date:", event.date)
        time_entry = label_input("Time:", event.time)
        venue_entry = label_input("Venue:", event.location)

        def send_invite():
            email = email_entry.get().strip()
            if email:
                invite = Invitation(name_entry.get(), surname_entry.get(), email, title_entry.get(),
                                    owner_entry.get(), date_entry.get(), time_entry.get(), venue_entry.get())
                self.invitations.append(invite)
                self.display_invitation(invite)
                messagebox.showinfo("Invitation Sent", f"Invitation sent to {email}")
                popup.destroy()
            else:
                messagebox.showwarning("Missing Info", "Please enter an email address.")

        tk.Button(popup, text="Send Invitation", command=send_invite,
                  bg="#28a745", fg="white", font=("Arial", 10, "bold")).pack(pady=20)

    def display_invitation(self, invitation):
        card = tk.Frame(self.invite_frame, bg="#ecf0f1", bd=1, relief="solid", padx=6, pady=4)
        card.pack(fill="x", padx=8, pady=6)

        tk.Label(card, text=f"{invitation.name} {invitation.surname}", font=("Arial", 10, "bold"), bg="#ecf0f1").pack(anchor="w")
        tk.Label(card, text=f"📧 {invitation.email}", bg="#ecf0f1").pack(anchor="w")
        tk.Label(card, text=f"🎉 {invitation.event_title} | 🕒 {invitation.time} | 📅 {invitation.date}", font=("Arial", 12), bg="#ecf0f1").pack(anchor="w")
        tk.Label(card, text=f"📍 {invitation.location}", bg="#ecf0f1").pack(anchor="w")

    # -- Other unchanged methods (toggle_main_content, help, calendar, events...) --
    # Paste the remaining methods from your current implementation here (like toggle_main_content, open_help_popup, etc.)


    def toggle_main_content(self):
        if self.main_content.winfo_ismapped():
            self.main_content.pack_forget()
        else:
            self.main_content.pack(side="left", fill="both", expand=True)

    def open_help_popup(self):
        popup = tk.Toplevel(self.root)
        popup.title("Need Help?")
        popup.geometry("350x200")
        popup.configure(bg="#f0f4f8")

        tk.Label(popup, text="💬 How can we help you?", font=("Arial", 13, "bold"), bg="#f0f4f8", fg="#2c3e50").pack(pady=10)
        question_entry = tk.Entry(popup, width=40, font=("Arial", 10))
        question_entry.pack(pady=10, padx=20)

        def submit_question():
            if question_entry.get().strip():
                messagebox.showinfo("Submitted", "Thanks! We'll get back to you soon.")
                popup.destroy()
            else:
                messagebox.showwarning("Empty", "Please enter a question.")

        tk.Button(popup, text="Submit", command=submit_question,
                  bg="#007bff", fg="white", font=("Arial", 10, "bold")).pack(pady=10)

    def show_calendar_with_highlighted_dates(self):
        popup = tk.Toplevel(self.root)
        popup.title("📅 Calendar View")
        popup.geometry("400x300")

        cal = Calendar(popup, selectmode="none", year=datetime.now().year,
                       month=datetime.now().month, date_pattern="yyyy-mm-dd")
        cal.pack(pady=20)

        for event in self.events:
            cal.calevent_create(datetime.strptime(event.date, "%Y-%m-%d"), event.title, 'event')
        cal.tag_config('event', background='lightgreen', foreground='black')

    def create_or_update_event(self):
        title = self.title_entry.get()
        date_str = self.date_entry.get()
        time = self.time_entry.get()
        location = self.location_entry.get()
        description = self.description_entry.get()
        budget = self.budget_entry.get()
        owner = self.owner_entry.get()
        priority = self.priority_var.get()

        if not title or not date_str or not time or not location:
            messagebox.showerror("Missing Info", "Title, date, time, and location are required.")
            return

        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter the date in YYYY-MM-DD format.")
            return

        if self.editing_event:
            self.editing_event.title = title
            self.editing_event.date = date_str
            self.editing_event.time = time
            self.editing_event.location = location
            self.editing_event.description = description
            self.editing_event.budget = budget
            self.editing_event.owner = owner
            self.editing_event.priority = priority
            self.refresh_list()
            messagebox.showinfo("Event Updated", "The event was successfully updated.")
            self.editing_event = None
            self.submit_button.config(text="CREATE EVENT")
        else:
            new_event = Event(title, date_str, time, location, description, budget, owner, priority)
            self.events.append(new_event)
            self.add_event_to_list(new_event)
            messagebox.showinfo("Event Created", "New event has been added.")

        self.clear_form()

    def add_event_to_list(self, event):
        card = tk.Frame(self.event_frame, bg="#ecf0f1", bd=1, relief="solid", padx=10, pady=8)
        card.pack(fill="x", pady=6, padx=5)

        tk.Label(card, text=f"📌 {event.title}", font=("Arial", 10, "bold"), bg="#ecf0f1", anchor="w").pack(anchor="w")
        info = f"📅 {event.date}  ⏰ {event.time}  📍 {event.location}"
        tk.Label(card, text=info, font=("Arial", 13, "bold"), fg="#555", bg="#ecf0f1", anchor="w").pack(anchor="w")

        details = f"📝 {event.description}\n💼 Owner: {event.owner}   💰 Budget: R{event.budget}   🔥 Priority: {event.priority}"
        tk.Label(card, text=details, font=("Arial", 10, "bold"), bg="#ecf0f1", justify="left", anchor="w", wraplength=500).pack(anchor="w", pady=4)

        button_frame = tk.Frame(card, bg="#ecf0f1")
        button_frame.pack(anchor="e", pady=(5, 0))

        tk.Button(button_frame, text="✏️ Edit", command=lambda e=event: self.load_event_for_edit(e),
                  bg="#ffc107", fg="black", font=("Arial", 9, "bold"), padx=6).pack(side="left", padx=(0, 6))

        tk.Button(button_frame, text="🗑️ Delete", command=lambda e=event: self.delete_event(e),
                  bg="#dc3545", fg="white", font=("Arial", 9, "bold"), padx=6).pack(side="left")

    def load_event_for_edit(self, event):
        self.editing_event = event
        self.selected_event_for_invitation = event
        self.title_entry.delete(0, tk.END)
        self.title_entry.insert(0, event.title)
        self.date_entry.set_date(event.date)
        self.time_entry.delete(0, tk.END)
        self.time_entry.insert(0, event.time)
        self.location_entry.delete(0, tk.END)
        self.location_entry.insert(0, event.location)
        self.description_entry.delete(0, tk.END)
        self.description_entry.insert(0, event.description)
        self.budget_entry.delete(0, tk.END)
        self.budget_entry.insert(0, event.budget)
        self.owner_entry.delete(0, tk.END)
        self.owner_entry.insert(0, event.owner)
        self.priority_var.set(event.priority)
        self.submit_button.config(text="UPDATE EVENT")

    def delete_event(self, event):
        confirm = messagebox.askyesno("Confirm Delete", f"Delete event '{event.title}'?")
        if confirm:
            self.events = [e for e in self.events if e.id != event.id]
            self.refresh_list()

    def refresh_list(self):
        for widget in self.event_frame.winfo_children():
            widget.destroy()
        for event in self.events:
            self.add_event_to_list(event)

    def clear_form(self):
        self.title_entry.delete(0, tk.END)
        self.date_entry.set_date(datetime.now())
        self.time_entry.delete(0, tk.END)
        self.location_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.budget_entry.delete(0, tk.END)
        self.owner_entry.delete(0, tk.END)
        self.priority_var.set("LOW")

    def cancel_edit(self):
        self.editing_event = None
        self.submit_button.config(text="CREATE EVENT")
        self.clear_form()


# -------------------- Run the App -------------------- #
if __name__ == "__main__":
    root = tk.Tk()
    app = EventPlannerApp(root)
    root.mainloop()
