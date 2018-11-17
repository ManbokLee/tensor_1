import tkinter as tk

class Label:
    def __init__(self, text, padx, pady):
        self.root = tk.Tk()
        self.label = tk.Label(self.root, text = text, padx = int(padx), pady = int(pady))
        self.label.pack()
        self.root.mainloop()
