import tkinter as tk
import random as rnd
import time
import pygame as pg
from custom_widgets import (CustomFrame,
                               CustomTitle, CustomSubtitle,
                               CustomLabel, CustomLabelv2,
                               CustomEntry, CustomButton)
from PIL import Image, ImageTk
# I used this tutorial to get images working in python: https://www.youtube.com/watch?v=UP_kOuCz88A

import threading
from playsound3 import playsound
# To get sound working, I used this: https://www.youtube.com/watch?v=ubcy_E6OjSU


class RPS_Menu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("Rock Paper Scissors")
        self.selection = None


        # This Menu has 6 rows in total
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
        self.rockimage = ImageTk.PhotoImage(Image.open("../images/angelo.png").resize((100, 100)))
        self.rocklabel = tk.Label(self.RPSFrame, image=self.rockimage)
        self.rocklabel.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        # paper image
        self.paperimage = ImageTk.PhotoImage(Image.open("../images/paper.png").resize((100, 100)))
        self.paperlabel = tk.Label(self.RPSFrame, image=self.paperimage)
        self.paperlabel.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
        # scissors image
        self.edwardimage = ImageTk.PhotoImage(Image.open("../images/edward.png").resize((100, 100)))
        self.edwardlabel = tk.Label(self.RPSFrame, image=self.edwardimage)
        self.edwardlabel.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)

        # preselect rock button
        self.selected_option = tk.StringVar(value="ROCK")

        # rock button
        self.rockbutton = tk.Radiobutton(self.RPSFrame, text="ROCK", command=self.rock,
                                         variable=self.selected_option, value="ROCK")
        self.rockbutton.grid(row=2, column=0, padx=10, pady=10)

        # paper button
        self.paperbutton = tk.Radiobutton(self.RPSFrame, text="PAPER", command=self.paper,
                                          variable=self.selected_option, value="PAPER")
        self.paperbutton.grid(row=2, column=1, padx=10, pady=10)

        # scissor button
        self.scissorbutton = tk.Radiobutton(self.RPSFrame, text="SCISSOR", command=self.scissors,
                                            variable=self.selected_option, value="SCISSOR")
        self.scissorbutton.grid(row=2, column=2, padx=10, pady=10)

        # GO button
        self.GObutton = tk.Button(self.RPSFrame, text="CONFIRM CHOICE", command=self.rockpapershootcallout)
        self.GObutton.grid(row=3, columnspan=3, padx=10, pady=10)



    # ==================================================================


    # opponent frame ===================================================
        self.OppFrame = CustomFrame(self, 2, 2)
        self.OppFrame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        # Robot Title
        self.opponentTitle = CustomTitle(self.OppFrame, "Your Robot Opponent")
        self.opponentTitle.grid(row=0, columnspan=2, sticky="nsew", padx=10, pady=10)

        #Robot image
        self.robotimage = ImageTk.PhotoImage(Image.open("../images/delamain.png").resize((100, 100)))
        self.robotlabel = tk.Label(self.OppFrame, image=self.robotimage)
        self.robotlabel.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        # Robot Speech Bubble
        self.speechbubbleimage = ImageTk.PhotoImage(Image.open("../images/speechbubble.png").resize((150, 150)))
        self.speechlabel = tk.Label(self.OppFrame, image=self.speechbubbleimage)
        self.speechlabel.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        # Robot Dialogue Box
        self.dialoguebox = CustomLabelv2(self.speechlabel, "Go on choom, call it.")
        self.dialoguebox.place(relx=0.5, rely=0.28, anchor="center")

# Winner Status Frame ===============================================
        self.WINNERSTATUSFRAME = CustomFrame(self, 1, columns=1)
        self.WINNERSTATUSFRAME.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        self.winnerstatus = CustomTitle(self.WINNERSTATUSFRAME, "CURRENT WINNER: N/A")
        self.winnerstatus.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

# ==================================================================

# Leaderboard Frame ================================================
        self.LEADERBOARDFRAME = CustomFrame(self, 4, 1)
        self.LEADERBOARDFRAME.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)

        self.LeaderboardTitle = CustomTitle(self.LEADERBOARDFRAME, "LEADERBOARD:")
        self.LeaderboardTitle.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        self.playerscore = 0
        self.playerlabel = CustomTitle(self.LEADERBOARDFRAME, f"PLAYER SCORE:{self.playerscore}")
        self.playerlabel.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

        self.robotscore = 0
        self.robotlabel = CustomTitle(self.LEADERBOARDFRAME, f"ROBOT SCORE:{self.robotscore}")
        self.robotlabel.grid(row=3, column=1, sticky="nsew", padx=10, pady=10)

        self.gobackbutton = tk.Button(self.LEADERBOARDFRAME,text="GO BACK", command=self.go_to_initial_frame)
        self.gobackbutton.grid(row=4, column=1, sticky="nsew", padx=10, pady=10)


# functions ========================================================

        pg.mixer.init()
        pg.mixer.music.load("../sfx/happymusic.mp3")
        pg.mixer.music.play(-1) #infinite loop
        pg.mixer.music.set_volume(0.1)

    def go_to_initial_frame(self):
        print("User clicked go back")
        from TITLE_Frames import TitleScreen
        self.destroy()
        self.parent.current_frame = TitleScreen(self.parent)
        self.parent.current_frame.pack()

    def play_sfx(self, soundfile):
        threading.Thread(target=lambda: playsound(soundfile), daemon=True).start()
        #^^^ I had no choice but to ask chatgpt here ^^^
        # because the GUI would freeze and not respond until the sound effect
        # was finished, and I wasn't sure how to fix it

    def rock(self):
        self.selection = "ROCK"
        self.play_sfx("../sfx/rocksfx.mp3")

    def paper(self):
        self.selection = "PAPER"
        self.play_sfx("../sfx/papersfx.mp3")

    def scissors(self):
        self.selection = "SCISSORS"
        self.play_sfx("../sfx/scissorsfx.mp3")

    def rockpapershootcallout(self):
        sequence = ["ROCK", "PAPER", "SCISSORS", "SHOOT"]
        self.play_sfx("../robotvoicelines/robot_shoot.mp3")
        def update_text(i=0):
            if i < len(sequence):
                self.dialoguebox.config(text=sequence[i])
                self.after(1000, lambda: update_text(i + 1))
            else:
                self.rollrandomitem()

        update_text()

        # ^^^ I also had to ask chatgpt here ^^^
        #I was running into a similar problem where
        #I tried to use the time library to delay each word to sync with the robot's voicelines but
        #it ended up freezing the whole GUI until the voicelines were complete

    def rollrandomitem(self):
        ITEMS = ["ROCK", "PAPER", "SCISSORS"]
        random = rnd.randint(0,2)
        if ITEMS[random] == self.selection:
            self.robotscore += 1
            self.playerscore += 1
            self.robotlabel.config(text=f"ROBOT SCORE: {self.robotscore}")
            self.playerlabel.config(text=f"PLAYER SCORE: {self.playerscore}")
            self.dialoguebox.config(text="WOW IT'S A TIE")
            self.winnerstatus.config(text="CURRENT WINNER: TIE")
            self.play_sfx("../robotvoicelines/robot_tie.mp3")


        #ROBOT WINS
        if ITEMS[random] == "PAPER" and self.selection == "ROCK":
            self.robotscore += 1
            self.robotlabel.config(text=f"ROBOT SCORE: {self.robotscore}")
            self.dialoguebox.config(text="HAHA I AM THE WINNER")
            self.winnerstatus.config(text="CURRENT WINNER: ROBOT")
            self.play_sfx("../sfx/OHNO.mp3")
            self.play_sfx("../robotvoicelines/robot_win.mp3")

        if ITEMS[random] == "ROCK" and self.selection == "SCISSORS":
            self.robotscore += 1
            self.robotlabel.config(text=f"ROBOT SCORE: {self.robotscore}")
            self.dialoguebox.config(text="HAHA I AM THE WINNER")
            self.winnerstatus.config(text="CURRENT WINNER: ROBOT")
            self.play_sfx("../sfx/OHNO.mp3")
            self.play_sfx("../robotvoicelines/robot_win.mp3")

        if ITEMS[random] == "SCISSORS" and self.selection == "PAPER":
            self.robotscore += 1
            self.robotlabel.config(text=f"ROBOT SCORE: {self.robotscore}")
            self.dialoguebox.config(text="HAHA I AM THE WINNER")
            self.winnerstatus.config(text="CURRENT WINNER: ROBOT")
            self.play_sfx("../sfx/OHNO.mp3")
            self.play_sfx("../robotvoicelines/robot_win.mp3")


        #ROBOT LOSES
        if ITEMS[random] == "ROCK" and self.selection == "PAPER":
            self.playerscore += 1
            self.playerlabel.config(text=f"PLAYER SCORE: {self.playerscore}")
            self.dialoguebox.config(text="OH NO I LOST")
            self.winnerstatus.config(text="CURRENT WINNER: HUMAN")
            self.play_sfx("../sfx/YAY.mp3")
            self.play_sfx("../robotvoicelines/robot_lose.mp3")

        if ITEMS[random] == "SCISSORS" and self.selection == "ROCK":
            self.playerscore += 1
            self.playerlabel.config(text=f"PLAYER SCORE: {self.playerscore}")
            self.dialoguebox.config(text="OH NO I LOST")
            self.winnerstatus.config(text="CURRENT WINNER: HUMAN")
            self.play_sfx("../sfx/YAY.mp3")
            self.play_sfx("../robotvoicelines/robot_lose.mp3")

        if ITEMS[random] == "PAPER" and self.selection == "SCISSORS":
            self.playerscore += 1
            self.playerlabel.config(text=f"PLAYER SCORE: {self.playerscore}")
            self.dialoguebox.config(text="OH NO I LOST")
            self.winnerstatus.config(text="CURRENT WINNER: HUMAN")
            self.play_sfx("../sfx/YAY.mp3")
            self.play_sfx("../robotvoicelines/robot_lose.mp3")





