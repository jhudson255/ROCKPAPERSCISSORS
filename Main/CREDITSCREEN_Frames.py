import tkinter as tk
from PIL import Image, ImageTk
import pygame as pg
# https://www.youtube.com/watch?v=xdkY6yhEccA tutorial used

class CreditScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("Welcome to Rock Paper Scissors (COOL EDITION)")
        self.selection = None


        for i in range(0,1):
            self.rowconfigure(i, weight=1)
        self.columnconfigure(1, weight=1)

        self.titleimage = ImageTk.PhotoImage(Image.open("../images/creditsscreen.png").resize((500, 500)))
        self.titlelabel = tk.Label(self, image=self.titleimage)
        self.titlelabel.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        self.gobackbutton = tk.Button(self.titlelabel, text="go back",
                                       command=self.load_RPSMENU,)
        self.gobackbutton.place(relx=0.8, rely=0.93, anchor="ne")


        # start title screen music
        pg.mixer.init()
        pg.mixer.music.load("../sfx/gymnopedieno1.mp3")
        pg.mixer.music.play(-1) #infinite loop

    def load_RPSMENU(self):
        from TITLE_Frames import TitleScreen
        pg.mixer.music.stop()
        self.destroy()
        self.parent.current_frame = TitleScreen(self.parent)
        self.parent.current_frame.pack()


