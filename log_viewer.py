import tkinter as tk
import tkinter.scrolledtext as st

# The LogViewer provides a separate window where users can view detailed logs
#  of the application's actions. To add logs, call the add_log method of the
#  LogViewer instance, passing the log text as an argument. You might need to
#  modify the process_posts and monitor_src functions to add logs for file
#  conversions, image updates, and audio generation.


class LogViewer(tk.Toplevel):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.title("Log Viewer")
        self.geometry("600x400")

        self.log_text = st.ScrolledText(self, wrap=tk.WORD, state='disabled')
        self.log_text.pack(expand=True, fill=tk.BOTH)

    def add_log(self, log_text):
        self.log_text.configure(state='normal')
        self.log_text.insert(tk.END, log_text + '\n')
        self.log_text.configure(state='disabled')
        self.log_text.see(tk.END)
