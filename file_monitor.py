import sys
import time
import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Import the necessary functions from mr-jekyll
from mrjekyll import process_markdown_file

class NewFileHandler(FileSystemEventHandler):
    def __init__(self, processor_function):
        self.processor_function = processor_function

    def on_created(self, event):
        if event.is_directory:
            return
        print(f"New file detected: {event.src_path}")
        self.processor_function(event.src_path)

def monitor_directory(path, processor_function):
    event_handler = NewFileHandler(processor_function)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python file_monitor.py <directory_to_watch>")
        sys.exit(1)

    directory_to_watch = sys.argv[1]

    def process_file(file_path):
        # Check if the file is a markdown file before processing
        if file_path.endswith(".md") or file_path.endswith(".markdown"):
            print(f"Processing {file_path}")
            process_markdown_file(file_path)
        else:
            print(f"Ignoring non-markdown file: {file_path}")

    monitor_directory(directory_to_watch, process_file)
