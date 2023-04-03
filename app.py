import tkinter as tk
from mrjekyll import process_markdown_file
from directory_selector import DirectorySelector
from status_bar import StatusBar
from settings_window import SettingsWindow
from help_window import HelpWindow
from menu_bar import create_menu_bar
from about_window import AboutWindow
from log_viewer import LogViewer
from progress_bar import ProgressBar
from monitor_src_module import monitor_src
import os
import shutil
import threading


def process_posts(src, dest, add_log):
    if not os.path.exists(dest):
        os.makedirs(dest)

    for root, dirs, files in os.walk(src):
        for file in files:
            if file.endswith('.md') or file.endswith('.markdown'):
                src_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(dest, file)

                shutil.copy2(src_file_path, dest_file_path)
                process_markdown_file(dest_file_path)
                add_log(f"Processed {src_file_path} -> {dest_file_path}")

def create_app(root):
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    src_selector = DirectorySelector(frame, "Source")
    src_selector.pack(fill=tk.X, padx=5, pady=5)

    dest_selector = DirectorySelector(frame, "Destination")
    dest_selector.pack(fill=tk.X, padx=5, pady=5)

    process_btn = tk.Button(frame, text="Process Posts", command=lambda: process_posts(src_selector.get_directory(), dest_selector.get_directory(), log_viewer.add_log))
    process_btn.pack()

    # feedback_window = feedback.FeedbackWindow(root)

    monitor_btn = tk.Button(frame, text="Monitor Source Folder", command=lambda: threading.Thread(target=monitor_src, args=(src_selector.get_directory(), dest_selector.get_directory(), log_viewer.add_log)).start())
    monitor_btn.pack()

    settings_window = SettingsWindow(root)
    settings_window.withdraw()

    settings_btn = tk.Button(frame, text="Settings", command=settings_window.deiconify)
    settings_btn.pack()

    progress = ProgressBar(frame)
    progress.pack(fill=tk.X, padx=5, pady=5)

    log_viewer = LogViewer(root)
    log_viewer.withdraw()

    log_btn = tk.Button(frame, text="Log Viewer", command=log_viewer.deiconify)
    log_btn.pack()

    help_window = HelpWindow(root)

    help_btn = tk.Button(frame, text="Help", command=help_window.deiconify)
    help_btn.pack()

    status_bar = StatusBar(root)
    status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    about_window = AboutWindow(root)

    create_menu_bar(root, settings_window.deiconify, help_window.deiconify, about_window.deiconify)

    return status_bar, progress #, feedback_window, log_viewer
