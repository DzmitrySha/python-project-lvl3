# Downloader

import os
import re
import requests
from urllib.parse import urlparse


def strip_url(url: str) -> str:
    parsed = urlparse(url)
    scheme = "%s://" % parsed.scheme
    return parsed.geturl().replace(scheme, '', 1)


def to_string(url: str) -> str:
    result = ''
    for char in strip_url(url):
        if not re.match('[a-zA-Z0-9]', char):
            result += '-'
        else:
            result += char

    return result + ".html"


def download(url: str, temp_folder=''):
    r = requests.get(url)

    file_path = os.path.join(temp_folder, to_string(url))

    with open(file_path, 'w') as file:
        file.write(r.text)
    # with open(file_path, 'r') as file:
    #     text = file.read()
    return file_path
