import tkinter as tk

# default background color
DEFAULT_BG = "light grey"

class CustomButton(tk.Button):
    def __init__(self, parent, btn_text, bg=DEFAULT_BG):
        super().__init__(parent, text=btn_text,
                         font=("Arial", "10", "bold"),
                         bg=bg)

class CustomTitle(tk.Label):
    def __init__(self, parent, title_text, bg=DEFAULT_BG):
        super().__init__(parent, text=title_text,
                         fg="black",
                         bg=bg,
                         font=("Arial", "25", "bold", "underline"))

class CustomSubtitle(tk.Label):
    def __init__(self, parent, title_text, bg=DEFAULT_BG):
        super().__init__(parent, text=title_text,
                         fg="grey",
                         bg=bg,
                         font=("Arial", "15"))

class CustomLabel(tk.Label):
    def __init__(self, parent, label_text, bg=DEFAULT_BG):
        super().__init__(parent, text=label_text,
                         fg="black",
                         bg=bg,
                         font=("Arial", "12"))

class CustomEntry(tk.Entry):
    def __init__(self, parent, bg=DEFAULT_BG):
        super().__init__(parent, bg=bg,
                         relief="solid")

class CustomFrame(tk.Frame):
    def __init__(self, parent, rows, columns, bg=DEFAULT_BG):
        super().__init__(parent, bg=bg, relief="solid")

        self.rows = rows
        self.columns = columns

        # configure the amount of rows + columns in the frame
        for r in range(rows):
            self.rowconfigure(r, weight=1)
        for c in range(columns):
            self.columnconfigure(c, weight=1)
