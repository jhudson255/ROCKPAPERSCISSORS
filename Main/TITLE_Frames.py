import tkinter as tk
from RPS_Frames import RPS_Menu
from custom_widgets import (CustomFrame,
                               CustomTitle, CustomSubtitle,
                               CustomLabel, CustomLabelv2,
                               CustomEntry, CustomButton)
from PIL import Image, ImageTk
from playsound3 import playsound
import threading

class TitleScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("Welcome to Rock Paper Scissors (COOL EDITION)")
        self.selection = None


        for i in range(0,1):
            self.rowconfigure(i, weight=1)
        self.columnconfigure(1, weight=1)

        self.titleimage = ImageTk.PhotoImage(Image.open("../images/titlescreen.png").resize((500, 500)))
        self.titlelabel = tk.Label(self, image=self.titleimage)
        self.titlelabel.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        self.newgamebutton = tk.Button(self.titlelabel, text="START GAME",
                                       command=self.load_RPSMENU,)
        self.newgamebutton.place(relx=0.5, rely=0.5, anchor="ne")

    def load_RPSMENU(self):
        self.parent.current_frame.destroy()
        self.parent.current_frame = RPS_Menu(self.parent)
        self.parent.current_frame.pack()

    def play_sfx(self, soundfile):
        threading.Thread(target=lambda: playsound(soundfile), daemon=True).start()