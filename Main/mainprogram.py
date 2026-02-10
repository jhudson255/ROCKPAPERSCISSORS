import tkinter as tk

from TITLE_Frames import TitleScreen
from RPS_Frames import RPS_Menu
class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Welcome to Rock Paper Scissors")
        self.geometry("700x700")
        self.configure(background = "light grey")

        self.current_frame = None
        self.load_first_page()

    def load_first_page(self):
        self.current_frame = TitleScreen(self)
        self.current_frame.pack()


# Main program
root = MainApplication()
root.mainloop()