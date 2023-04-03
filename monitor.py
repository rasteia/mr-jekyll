import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MonitorHandler(FileSystemEventHandler):
    def __init__(self, src_dir, callback):
        super().__init__()
        self.src_dir = src_dir
        self.callback = callback

    def on_created(self, event):
        if event.src_path.endswith('.md'):
            self.callback(event.src_path)

    def start_monitoring(self):
        observer = Observer()
        observer.schedule(self, path=self.src_dir, recursive=False)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()

        observer.join()

def monitor_src():
    src_dir = filedialog.askdirectory(title="Select Source Directory")
    handler = monitor.MonitorHandler(src_dir, process_file)
    threading.Thread(target=handler.start_monitoring).start()
