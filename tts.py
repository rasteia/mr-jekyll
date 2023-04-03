import os
from gtts import gTTS

DEFAULT_AUDIO = "default_audio.mp3"

def update_default_audio(posts_dir):
    for root, _, files in os.walk(posts_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                    if DEFAULT_AUDIO in content:
                        tts = gTTS(content, lang='en')
                        tts.save(os.path.join(posts_dir, f"{file[:-3]}_audio.mp3"))
