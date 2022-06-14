# Downloader

import os
import re
import requests
from urllib.parse import urlparse


def strip_url_scheme(url: str) -> str:
    """Strip scheme ('http://' or 'https://') from url"""
    parsed_url = urlparse(url)
    scheme = f"{parsed_url.scheme}://"
    return parsed_url.geturl().replace(scheme, '', 1)


def make_html_filename(url: str) -> str:
    """Make html filename from url"""
    indent = '-'
    mask = '[a-zA-Z0-9]'
    strip_url = strip_url_scheme(url)

    result = "".join(char if re.match(mask, char) else indent
                     for char in strip_url)

    return result + ".html" if not os.path.splitext(url)[1] else result


def download(url: str, temp_folder='') -> str:
    r = requests.get(url)
    file_path = os.path.join(temp_folder, make_html_filename(url))

    with open(file_path, 'w') as file:
        file.write(r.text)

    return file_path
