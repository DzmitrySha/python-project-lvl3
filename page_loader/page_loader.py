# Downloader

import os
import re
import requests
from urllib.parse import urlparse


def strip_scheme(url: str) -> str:
    parsed_url = urlparse(url)
    scheme = f"{parsed_url.scheme}://"
    return parsed_url.geturl().replace(scheme, '', 1)


def to_string(url: str) -> str:
    indent = '-'
    reg = '[a-zA-Z0-9]'
    strip_url = strip_scheme(url)

    result = "".join(char if re.match(reg, char) else indent
                     for char in strip_url)

    return result + ".html" if not os.path.splitext(url)[1] else result


def download(url: str, temp_folder=''):
    r = requests.get(url)
    file_path = os.path.join(temp_folder, to_string(url))

    with open(file_path, 'w') as file:
        file.write(r.text)

    return file_path
