# Downloader

import os
import requests


def download(url: str, temp_folder='var/tmp'):
    r = requests.get(url)
    file_path = os.path.join(os.path.dirname(__file__),
                             temp_folder, 'text_file')
    with open(file_path, 'w') as file:
        file.write(r.text)
    with open(file_path, 'r') as file:
        text = file.read()
    return text
