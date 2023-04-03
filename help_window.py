
# help_window.py: A module to create a 'Help' window providing users with instructions on how to use the application and information on its features.
# The HelpWindow provides a separate window where users can find instructions and
# information about the application's features. You can update the help text in 
# the help_text


import tkinter as tk
import tkinter.scrolledtext as st

class HelpWindow(tk.Toplevel):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.title("Help")
        self.geometry("600x400")

        help_text = """
This application processes Jekyll posts and provides additional features like monitoring for new files and generating images and audio.

To use the application, follow these steps:

1. Select the source directory containing your Markdown files.
2. Select the destination directory where processed files will be stored.
3. Click "Process Posts" to process the Markdown files.
4. (Optional) Click "Monitor Source Folder" to start monitoring the source folder for new files.
5. (Optional) Use the "Settings" button to configure default paths and other settings.
6. (Optional) Use the "Log Viewer" button to view detailed logs of the application's actions.

Features:
- Process and move Markdown files to properly formatted blog posts in _posts
- Monitor the source folder for new files and automatically process them
- Generate and update images for posts with default images
- Convert post text to audio files and update the default audio in the post
"""

        self.help_text_widget = st.ScrolledText(self, wrap=tk.WORD, state='normal')
        self.help_text_widget.insert(tk.END, help_text)
        self.help_text_widget.configure(state='disabled')
        self.help_text_widget.pack(expand=True, fill=tk.BOTH)
