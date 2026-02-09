import tkinter as tk
#import random as rnd
from custom_widgets import (CustomFrame,
                               CustomTitle, CustomSubtitle,
                               CustomLabel, CustomEntry)

class RPS_Menu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("RPS_Menu")


        # This Menu has 5 rows in total
        for i in range(0,5):
            self.rowconfigure(i, weight=1)

        for i in range(0,2):
            self.columnconfigure(i, weight=1)


        # title frame ======================================================
        self.TitleFrame = CustomFrame(self, 2, 1)
        self.TitleFrame.grid(row=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        # title
        self.Title = CustomTitle(self.TitleFrame, "Rock Paper Scissors")
        self.Title.grid(row=0)
        # subtitle
        self.Subtitle = CustomSubtitle(self.TitleFrame, "A generic rock paper scissors application")
        self.Subtitle.grid(row=1)
        # ==================================================================

        # rock paper or scissors selection frame ===========================
        self.RPSFrame = CustomFrame(self, 4, 3)
        self.RPSFrame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        # YOUR MOVE label
        self.yourmove = CustomLabel(self.RPSFrame, "YOUR MOVE")




