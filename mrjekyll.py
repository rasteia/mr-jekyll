import os
import re
import datetime
import shutil
from slugify import slugify
TEMPLATE_HEAD_PATH = "./templatehead.txt"

def read_template_head():
    with open(TEMPLATE_HEAD_PATH, "r") as file:
        return file.read()

def process_markdown_file(src_file_path, dest_file_path):
    template_head = read_template_head()

    # Get the current date and time
    current_datetime = datetime.datetime.now()
    current_date = current_datetime.strftime('%Y-%m-%d')
    current_time = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

    # Extract the title from the file name
    file_name = os.path.basename(src_file_path)
    title = os.path.splitext(file_name)[0]

    # Clean up the title and generate a valid slug
    cleaned_title = re.sub(r"[^\w\s-]", "", title)
    cleaned_title = re.sub(r"\s+", " ", cleaned_title).strip()
    slug = slugify(cleaned_title, max_length=80)

    # Update the filename with proper Jekyll format
    new_file_name = f"{current_date}-{slug}.md"

    # Update the destination file path with new file name
    dest_file_path = os.path.join(dest_file_path, new_file_name)

    # Read the original file content
    with open(src_file_path, "r") as file:
        content = file.read()

    # Update the file content with the title and date
    updated_template_head = template_head.format(title=cleaned_title, date=current_time)
    updated_content = updated_template_head + "\n" + content

    # Write the updated content to the new file
    with open(dest_file_path, "w") as file:
        file.write(updated_content)

    # Remove the original file
    os.remove(src_file_path)

    print(f"Processed {src_file_path} -> {dest_file_path}")




