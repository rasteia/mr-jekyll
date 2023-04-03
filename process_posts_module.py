from tkinter import filedialog
import newpost
import newimage
import tts

def process_posts(src_dir, dest_dir, log_func=lambda x: None):
    for md_file in glob.glob(os.path.join(src_dir, "*.md")):
        src_filepath = md_file
        filename = os.path.basename(src_filepath)
        dest_filepath = os.path.join(dest_dir, filename)
        shutil.move(src_filepath, dest_filepath)
        log_func(f"Processed post: {src_filepath} -> {dest_filepath}")