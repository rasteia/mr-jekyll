# about_window.py: Here's an about_window.py module that creates an 'About' window
# displaying information about the application, its version, and the .

# The AboutWindow class provides a separate window where users can find 
# information about the application, its version, and the developers. 
# Update the "Developed by" label with the appropriate developer name(s).

import tkinter as tk

class AboutWindow(tk.Toplevel):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.title("About")
        self.geometry("300x200")

        app_name = tk.Label(self, text="Jekyll Post Processor", font=("Arial", 16, "bold"))
        app_name.pack(pady=10)

        app_version = tk.Label(self, text="Version: 1.0.0", font=("Arial", 12))
        app_version.pack()

        app_developers = tk.Label(self, text="Developed by: Not Sure", font=("Arial", 12))
        app_developers.pack(pady=10)

        close_button = tk.Button(self, text="Close", command=self.destroy)
        close_button.pack(pady=5)
