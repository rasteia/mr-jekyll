import tkinter as tk
from tkinter import filedialog, Text

class FeedbackWindow:
    def __init__(self, root):
        self.root = root
        self.text = Text(self.root, wrap='word', height=15, width=80)
        self.text.pack(padx=10, pady=10)
        self.text.config(state='disabled')

    def update_text(self, message):
        self.text.config(state='normal')
        self.text.insert('end', message + '\n')
        self.text.config(state='disabled')
        self.text.see('end')
