import tkinter as tk
from tkinter import filedialog

class DirectorySelector(tk.Frame):
    def __init__(self, master, label_text, **kwargs):
        super().__init__(master, **kwargs)

        self.label = tk.Label(self, text=label_text)
        self.label.pack(side=tk.LEFT)

        self.entry = tk.Entry(self)
        self.entry.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.browse_button = tk.Button(self, text="Browse", command=self.browse_directory)
        self.browse_button.pack(side=tk.LEFT)

    def browse_directory(self):
        selected_directory = filedialog.askdirectory(title=f"Select {self.label['text']} Directory")
        self.entry.delete(0, tk.END)
        self.entry.insert(0, selected_directory)

    def get_directory(self):
        return self.entry.get()
