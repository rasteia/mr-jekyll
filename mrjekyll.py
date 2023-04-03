import os
import re
import datetime
from slugify import slugify

def read_template_head():
    with open("templatehead.txt", "r") as file:
        return file.read()

def process_markdown_file(file_path):
    template_head = read_template_head()

    # Get the current date and time
    current_datetime = datetime.datetime.now()
    current_date = current_datetime.strftime('%Y-%m-%d')
    current_time = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

    # Extract the title from the file name
    file_name = os.path.basename(file_path)
    title = os.path.splitext(file_name)[0]

    # Clean up the title and generate a valid slug
    cleaned_title = re.sub(r"[^\w\s-]", "", title)
    cleaned_title = re.sub(r"\s+", " ", cleaned_title).strip()
    slug = slugify(cleaned_title, max_length=80)

    # Update the filename with proper Jekyll format
    new_file_name = f"{current_date}-{slug}.md"
    new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)

    # Read the original file content
    with open(file_path, "r") as file:
        content = file.read()

    # Update the file content with the title and date
    updated_template_head = template_head.format(title=cleaned_title, date=current_time)
    updated_content = updated_template_head + "\n" + content

    # Write the updated content to the new file
    with open(new_file_path, "w") as file:
        file.write(updated_content)

    # Remove the original file
    os.remove(file_path)

    print(f"Processed {file_path} -> {new_file_path}")
