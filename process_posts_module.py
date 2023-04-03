from tkinter import filedialog
import newpost
import newimage
import tts

def process_posts(src_dir, dest_dir, log_func=None):
    newpost.process_new_posts(src_dir, dest_dir)
    newimage.update_default_images(dest_dir)
    tts.update_default_audio(dest_dir)
    if log_func:
        log_func(f"Processed post: {src_file} -> {dest_file}")
