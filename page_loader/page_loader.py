# Downloader

import os
import re
import requests
from urllib.parse import urlparse


def cut_url_scheme(url: str) -> str:
    """Cut scheme ('http://' or 'https://') from url."""
    parsed_url = urlparse(url)
    scheme = f"{parsed_url.scheme}://"
    return parsed_url.geturl().replace(scheme, '', 1)


def url_to_filename(url: str) -> str:
    """Make file-name.html from url."""
    indent = '-'
    mask = '[a-zA-Z0-9]'
    ext = ".html"
    strip_url = cut_url_scheme(url)
    result = "".join(char if re.match(mask, char) else indent
                     for char in strip_url)
    return result + ext if os.path.splitext(url)[1] != ext else result


def write_to_file(file_path, text):
    """Write text to file."""
    with open(file_path, 'w') as file:
        file.write(text)


def download(url: str, temp_folder='') -> str:
    """Download html page, save to exist specified folder."""
    response = requests.get(url)
    filename = url_to_filename(url)
    file_path = os.path.join(temp_folder, filename)
    write_to_file(file_path, response.text)
    return file_path
