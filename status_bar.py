import tkinter as tk

class StatusBar(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = tk.Label(self, text="Status: Idle", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.label.pack(fill=tk.X)

    def update_status(self, status_text):
        self.label.config(text=f"Status: {status_text}")
        self.label.update_idletasks()
