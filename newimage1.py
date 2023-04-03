import os
from PIL import Image

DEFAULT_IMAGE = "default_image.jpg"

def update_default_images(posts_dir):
    for root, _, files in os.walk(posts_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                    if DEFAULT_IMAGE in content:
                        # Generate the new image using some custom logic
                        new_image = Image.new('RGB', (300, 300), color='red')
                        new_image.save(os.path.join(posts_dir, f"{file[:-3]}_image.jpg"))
