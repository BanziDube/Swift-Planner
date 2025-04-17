import tkinter as tk
from landing_page import show_landing_page


def main():
    root = tk.Tk()
    root.title("Swift Planner")
    root.geometry("800x600")
    show_landing_page(root)
    root.mainloop()


if __name__ == "__main__":
    main()
