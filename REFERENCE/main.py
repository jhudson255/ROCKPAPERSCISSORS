import tkinter as tk
from framesREF import DiceMenu

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Welcome to Dice Roll")
        self.geometry("1000x1000")
        self.configure(background = "white")

        self.current_frame = None
        self.load_first_page()

    def load_first_page(self):
        self.current_frame = DiceMenu(self)
        self.current_frame.pack()

# Main program
root = MainApplication()
root.mainloop()