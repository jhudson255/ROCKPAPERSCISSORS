import tkinter as tk
from frames import RPS_Menu

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Welcome to Rock Paper Scissors")
        self.geometry("1000x1000")
        self.configure(background = "light grey")

        self.current_frame = None
        self.load_first_page()

    def load_first_page(self):
        self.current_frame = RPS_Menu(self)
        self.current_frame.pack()

# Main program
root = MainApplication()
root.mainloop()