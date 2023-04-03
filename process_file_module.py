from tkinter import filedialog
import newpost
import newimage
import tts

def process_file(src_file, feedback_window):
    src_dir = filedialog.askdirectory(title="Select Source Directory")
    dest_dir = filedialog.askdirectory(title="Select Destination Directory (_posts)")

    newpost.process_new_posts(src_dir, dest_dir)
    newimage.update_default_images(dest_dir)
    tts.update_default_audio(dest_dir)

    feedback_window.update_text(f"Processed: {src_file}")
