import os
import shutil
from datetime import datetime

def process_new_posts(src_dir, dest_dir):
    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                    timestamp = datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S')
                    new_filename = f"{timestamp}-{file}"
                    dest_path = os.path.join(dest_dir, new_filename)

                shutil.move(file_path, dest_path)
