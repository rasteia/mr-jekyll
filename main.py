import tkinter as tk
from app import create_app

root = tk.Tk()
root.title("Jekyll Post Processor")

feedback_window = create_app(root)

root.mainloop()
