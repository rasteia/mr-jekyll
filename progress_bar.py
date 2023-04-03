import tkinter as tk
from tkinter import ttk

# Progress bar To add logs, call the add_log method of the LogViewer instance, passing 
# #the log text as an argument. You might need to modify the process_posts
# and monitor_src functions to add logs for file conversions, image updates,
#  and audio generation.

class ProgressBar(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self, variable=self.progress_var, maximum=100)
        self.progress_bar.pack(fill=tk.X, expand=True)

    def update_progress(self, value):
        self.progress_var.set(value)
        self.progress_bar.update_idletasks()

    def reset_progress(self):
        self.progress_var.set(0)
        self.progress_bar.update_idletasks()
