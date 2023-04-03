import os
import shutil
import re
from datetime import datetime
from typing import Tuple
from pathlib import Path

def get_post_title(file_path: str) -> str:
    """
    Get the post title from the given file path.

    Args:
    - file_path (str): The path of the file.

    Returns:
    - str: The post title.
    """
    title = os.path.basename(file_path)
    title, _ = os.path.splitext(title)
    return title


def get_dest_file_path(file_path: str, dest_dir_path: str) -> Tuple[str, str]:
    """
    Get the destination file path for the given file.

    Args:
    - file_path (str): The path of the file.
    - dest_dir_path (str): The path of the destination directory.

    Returns:
    - Tuple[str, str]: The destination directory path and the destination file name.
    """
    title = get_post_title(file_path)
    date_str = datetime.now().strftime("%Y-%m-%d")
    new_file_name = f"{date_str}-{title.lower().replace(' ', '-')}.md"
    dest_file_path = os.path.join(dest_dir_path, new_file_name)
    return dest_dir_path, dest_file_path


def process_markdown_file(src_file_path: str, dest_dir_path: str) -> None:
    """
    Process the given markdown file.

    Args:
    - src_file_path (str): The path of the markdown file.
    - dest_dir_path (str): The path of the destination directory.
    """
    _, dest_file_path = get_dest_file_path(src_file_path, dest_dir_path)
    with open(src_file_path, "r", encoding="utf-8") as src_file:
        content = src_file.read()

    # Replace all images with new relative paths
    pattern = r"(!\[[^\]]*\]\((?!http)[^)]+\))"
    for match in re.findall(pattern, content):
        image_path = match.split("(")[1].split(")")[0]
        image_name = os.path.basename(image_path)
        new_image_path = os.path.join(os.path.dirname(dest_file_path), "assets", "images", image_name)
        content = content.replace(image_path, new_image_path)

    with open(dest_file_path, "w", encoding="utf-8") as dest_file:
        dest_file.write(content)

    # Move the source file to the processed directory
    processed_dir_path = os.path.join(os.path.dirname(src_file_path), "processed")
    os.makedirs(processed_dir_path, exist_ok=True)
    shutil.move(src_file_path, os.path.join(processed_dir_path, os.path.basename(src_file_path)))


def process_new_file(file_path: str, dest_dir_path: str) -> None:
    """
    Process the new file with the given path.

    Args:
    - file_path (str): The path of the new file.
    - dest_dir_path (str): The path of the destination directory.
    """
    if file_path.endswith(".md"):
        process_markdown_file(file_path, dest_dir_path)
