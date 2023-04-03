import tkinter as tk
from directory_selector import DirectorySelector

class SettingsWindow(tk.Toplevel):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.title("Settings")
        self.geometry("400x200")

        frame = tk.Frame(self)
        frame.pack(padx=10, pady=10)

        self.src_selector = DirectorySelector(frame, "Default Source")
        self.src_selector.pack(fill=tk.X, padx=5, pady=5)

        self.dest_selector = DirectorySelector(frame, "Default Destination")
        self.dest_selector.pack(fill=tk.X, padx=5, pady=5)

        # Add more settings here as needed

        save_btn = tk.Button(frame, text="Save", command=self.save_settings)
        save_btn.pack()

    def save_settings(self):
        # Save settings, for example, using a JSON configuration file
        # You can implement your preferred method to store these settings
        self.destroy()
