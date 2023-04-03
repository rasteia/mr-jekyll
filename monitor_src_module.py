from tkinter import filedialog
import threading
import monitor
from process_file_module import process_file

def monitor_src(src_dir, log_func=None):
    src_dir = filedialog.askdirectory(title="Select Source Directory")
    handler = monitor.MonitorHandler(src_dir, lambda src_file: process_file(src_file, feedback_window))
    threading.Thread(target=handler.start_monitoring).start()
    if log_func:
        log_func(f"New file detected: {src_file}")
