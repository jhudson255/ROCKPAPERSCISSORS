import tkinter as tk
from PIL import Image, ImageTk
import pygame as pg
# https://www.youtube.com/watch?v=xdkY6yhEccA tutorial used

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
                                       command=self.load_RPSMENU, pady=10)
        self.newgamebutton.place(relx=0.5, rely=0.4, anchor="ne")
        self.creditsbutton = tk.Button(self.titlelabel, text="credits",
                                       command=self.load_CREDITSCREEN, pady=10)
        self.creditsbutton.place(relx=0.5, rely=0.5, anchor="ne")


        # start title screen music
        pg.mixer.init()
        pg.mixer.music.load("../sfx/tavernmusic.mp3")
        pg.mixer.music.play(-1) #infinite loop

    def load_RPSMENU(self):
        from RPS_Frames import RPS_Menu
        pg.mixer.music.stop()
        self.parent.current_frame.destroy()
        self.parent.current_frame = RPS_Menu(self.parent)
        self.parent.current_frame.pack()

    def load_CREDITSCREEN(self):
        from CREDITSCREEN_Frames import CreditScreen
        pg.mixer.music.stop()
        self.parent.current_frame.destroy()
        self.parent.current_frame = CreditScreen(self.parent)
        self.parent.current_frame.pack()

