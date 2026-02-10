import tkinter as tk
#import random as rnd
from custom_widgets import (CustomFrame,
                               CustomTitle, CustomSubtitle,
                               CustomLabel, CustomEntry, CustomButton)
from PIL import Image, ImageTk
# I used this tutorial to get images working in python: https://www.youtube.com/watch?v=UP_kOuCz88A

from playsound3 import playsound
# To get sound working, I used this: https://www.youtube.com/watch?v=ubcy_E6OjSU

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
        self.yourmove = CustomLabel(self.RPSFrame, "Rock, Paper or Scissors, whatever shall it be?")
        self.yourmove.grid(row=0, columnspan=3, sticky="nsew", padx=10, pady=10)
        # rock image
        self.rockimage = ImageTk.PhotoImage(Image.open("angelo.png").resize((100, 100)))
        self.rocklabel = tk.Label(self.RPSFrame, image=self.rockimage)
        self.rocklabel.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        # paper image
        self.paperimage = ImageTk.PhotoImage(Image.open("paper.png").resize((100, 100)))
        self.paperlabel = tk.Label(self.RPSFrame, image=self.paperimage)
        self.paperlabel.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
        # scissors image
        self.edwardimage = ImageTk.PhotoImage(Image.open("edward.png").resize((100, 100)))
        self.edwardlabel = tk.Label(self.RPSFrame, image=self.edwardimage)
        self.edwardlabel.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)

        # rock button
        self.rockbutton = CustomButton(self.RPSFrame, "Rock Paper Scissors")





