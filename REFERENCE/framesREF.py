import tkinter as tk
import random as rnd
from custom_widgetsREF import (CustomFrame,
                               CustomTitle, CustomSubtitle,
                               CustomLabel, CustomEntry)

class DiceMenu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("Dice Menu")

        for i in range(0,4):
            self.rowconfigure(i, weight=1)
        self.columnconfigure(0, weight=1)

        # title frame ===========================
        self.TitleFrame = CustomFrame(self, 2, 1)
        self.TitleFrame.grid(row = 0, column=0, sticky = "nsew", padx=10, pady=10)
        # title
        self.Title = CustomTitle(self.TitleFrame, "Dice Roll")
        self.Title.grid(row = 0)
        # subtitle
        self.Subtitle = CustomSubtitle(self.TitleFrame, "A Generic dice roller")
        self.Subtitle.grid(row = 1)
        # =======================================

        # options frame =========================
        self.OptionsFrame = CustomFrame(self, 3, 2)
        self.OptionsFrame.grid(row = 1, column=0, sticky = "nsew", padx=10, pady=10)


        # no. sides
        self.NumSides = CustomLabel(self.OptionsFrame, "Number of sides")
        self.NumSides.grid(row = 0 ,column = 0)
        # enter box
        self.EntryBoxLeft = CustomEntry(self.OptionsFrame)
        self.EntryBoxLeft.grid(row = 1, column = 0)
        # submit button left
        self.SubmitLeft = tk.Button(self.OptionsFrame, text = "Submit", command= self.set_sides)
        self.SubmitLeft.grid(row = 2, column = 0)


        # no. rolls
        self.NumRolls = CustomLabel(self.OptionsFrame, "Number of rolls")
        self.NumRolls.grid(row=0, column = 1)
        # enter box
        self.EntryBoxRight = tk.Entry(self.OptionsFrame)
        self.EntryBoxRight.grid(row=1, column=1)
        # submit button left
        self.SubmitRight = tk.Button(self.OptionsFrame, text="Submit", command= self.set_rolls)
        self.SubmitRight.grid(row=2, column=1)
        # =======================================

        # ROLL Frame =====================
        self.RollFrame = CustomFrame(self,0,2)
        self.RollFrame.grid(row=2, column=0, sticky = "nsew", padx=10, pady=10)
        # ROLL Button
        self.RollButton = tk.Button(self.RollFrame, text= "ROLL", command = self.dice)
        self.RollButton.grid(row=0, column=0)
        # List Box
        self.listbox = tk.Listbox(self.RollFrame)
        self.listbox.grid(row = 0, column = 1, sticky = "nsew")

        # Gamble Button  ====================
        self.GambleFrame = CustomFrame(self, 1, 1)
        self.GambleButton = tk.Button(self.GambleFrame, text="CLICK TO GAMBLE",
                                      command = self.load_second_frame)
        self.GambleButton.grid(row=0, column=0)
        self.GambleFrame.grid(row = 3, column = 0, padx=10, pady=10)


    def set_sides(self):
        self.num_sides = int(self.EntryBoxLeft.get())


    def set_rolls(self):
        self.num_rolls = int(self.EntryBoxRight.get())

    def dice(self):
        self.listbox.delete(0, tk.END)

        numsides = self.num_sides
        numrolls = self.num_rolls

        for i in range(0,numrolls+1):
            random = rnd.randint(1, numsides)
            random = str(f"Roll{i}: "+f"{random}")

            self.listbox.insert(tk.END, random)







    def load_second_frame(self):
        self.parent.current_frame.destroy()

        self.parent.current_frame = GambleMode(self.parent)
        self.parent.current_frame.pack()

class GambleMode(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        for i in range(0,4):
            self.rowconfigure(i, weight=1)
        self.columnconfigure(1, weight=1)

        # slot machine
        self.slotmachine_frame = CustomFrame(self, 2, 3)
        self.slotmachine_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.title = CustomTitle(self.slotmachine_frame, "It's gambling time")
        self.title.grid(row = 0, column=1, sticky = "nsew")
        self.subtitle = CustomSubtitle(self.slotmachine_frame, "fun fact: did you know 90% of gamblers"
                                                               " quit just before they hit it big?")
        self.subtitle.grid(row=1, column=1, sticky="nsew", pady=10, padx=10)

        self.firstdigit = tk.Label(self.slotmachine_frame, text = "X",
                                   relief = "solid",
                                   borderwidth = 10,
                                   bg = "white", fg = "black")
        self.firstdigit.grid(row = 2, column = 0)

        self.seconddigit = tk.Label(self.slotmachine_frame, text="X",
                                    relief = "solid",
                                    borderwidth=10,
                                    bg="white", fg="black")
        self.seconddigit.grid(row=2, column=1)

        self.thirddigit = tk.Label(self.slotmachine_frame, text="X",
                                   relief="solid",
                                   borderwidth=10,
                                   bg="white", fg="black")
        self.thirddigit.grid(row=2, column=2)

        # options frame
        self.options_frame = CustomFrame(self, 2, 3)
        self.options_frame.grid(row=1, column=0, sticky = "nsew", padx=10, pady=10)

        self.GambleButton = tk.Button(self.options_frame, text="LET'S GAMBLE",
                                      command = self.lets_gamble)
        self.GambleButton.grid(row=0, column=0)
        self.winstatus = tk.Label(self.options_frame, text="N/A", fg="red",
                                  bg="light grey",
                                  font=("bold", "50"))
        self.winstatus.grid(row=0, column=1)
        self.GoBackButton = tk.Button(self.options_frame, text="Go Back",
                             command=self.go_to_initial_frame)
        self.GoBackButton.grid(row=0, column=2)

        self.debt = 0
        self.debtstatus = tk.Label(self.options_frame,
                                  text=f"bank account: £{self.debt}",
                                  fg="black", bg="light grey",
                                  font=("bold", "50"))
        self.debtstatus.grid(row=1, column=1)





    def lets_gamble(self):
        debt = self.debt
        # number rolling
        first = rnd.randint(1, 9)
        second = rnd.randint(1, 9)
        third = rnd.randint(1, 9)

        # configure the slot machine
        self.firstdigit.config(text=str(first))
        self.seconddigit.config(text=str(second))
        self.thirddigit.config(text=str(third))

        # if all three match then update win status
        if first == second == third:
            self.debt = self.debt + 1000000
            self.winstatus.config(text="JACKPOT!!!!", fg="green")
            self.debtstatus.config(text=f"bank account: £{self.debt}",)


        else:
            self.debt = self.debt - 100
            self.winstatus.config(text="try again bucko", fg="red")
            self.debtstatus.config(text=f"bank account: £{self.debt}")



    def go_to_initial_frame(self):
        self.parent.current_frame.destroy()

        self.parent.current_frame = DiceMenu(self.parent)
        self.parent.current_frame.pack()

# i couldnt be bothered to animate the slot machine
