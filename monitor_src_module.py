from tkinter import filedialog
import threading
import os
import time
from process_file_module import process_file
from feedback import FeedbackWindow
from file_monitor import monitor_directory
from mrjekyll import process_markdown_file

def monitor_src(src_dir, dest_dir, add_log, delay=5):
    def on_new_file(file_path):
        if file_path.endswith('.md') or file_path.endswith('.markdown'):
            dest_file_path = os.path.join(dest_dir, os.path.basename(file_path))
            process_markdown_file(file_path, dest_file_path)
            add_log(f"Processed {file_path} -> {dest_file_path}")

    print("Monitoring", src_dir)
    for event in monitor_directory(src_dir, on_new_file):
        if event is not None:
            time.sleep(delay)

