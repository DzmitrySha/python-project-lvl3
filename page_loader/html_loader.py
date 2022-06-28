"""HTML loader module."""

import os
import requests
from page_loader.naming import make_name


def write_to_file(file_path: str, text: str):
    """Write text to file."""
    with open(file_path, 'w') as file:
        file.write(text)


def html_download(url: str, temp_folder='') -> str:
    """Download html page, save to exist specified folder."""
    response_text = requests.get(url).text

    filename = make_name(url, ext=".html")
    file_path = os.path.join(temp_folder, filename)

    write_to_file(file_path, response_text)
    return file_path
