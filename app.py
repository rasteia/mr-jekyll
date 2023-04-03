import tkinter as tk
from process_posts_module import process_posts
from monitor_src_module import monitor_src
from directory_selector import DirectorySelector
from status_bar import StatusBar
from settings_window import SettingsWindow
from progress_bar import ProgressBar
from help_window import HelpWindow
from menu_bar import create_menu_bar
from about_window import AboutWindow
# import feedback
# from log_viewer import LogViewer

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

    # monitor_btn = tk.Button(frame, text="Monitor Source Folder", command=lambda: monitor_src(src_selector.get_directory(), log_viewer.add_log))
    # monitor_btn.pack()

    settings_window = SettingsWindow(root)
    settings_window.withdraw()

    settings_btn = tk.Button(frame, text="Settings", command=settings_window.deiconify)
    settings_btn.pack()

    progress = ProgressBar(frame)
    progress.pack(fill=tk.X, padx=5, pady=5)

    #log_viewer = LogViewer(root)
    # log_viewer.withdraw()

    # log_btn = tk.Button(frame, text="Log Viewer", command=log_viewer.deiconify)
    # log_btn.pack()

    help_window = HelpWindow(root)

    help_btn = tk.Button(frame, text="Help", command=help_window.deiconify)
    help_btn.pack()

    status_bar = StatusBar(root)
    status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    about_window = AboutWindow(root)


    create_menu_bar(root, settings_window.deiconify, help_window.deiconify, about_window.deiconify)

    return status_bar, progress #, feedback_window, log_viewer
