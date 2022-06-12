# Downloader

import os
import requests
from urllib.parse import urlparse


def strip_scheme(url: str) -> str:
    parsed = urlparse(url)
    scheme = "%s://" % parsed.scheme
    if not url.endswith(".html"):
        return parsed.geturl().replace(scheme, '', 1) + ".html"
    # [a - zA - Z0 - 9] , import re
    return parsed.geturl().replace(scheme, '', 1)


def url_to_string(url: str) -> str:
    return str(url)


def download(url: str, temp_folder=''):
    r = requests.get(url)
    # url_string = url_to_string(url)
    file_path = os.path.join(os.path.dirname(__file__),
                             temp_folder, 'result_file')
    with open(file_path, 'w') as file:
        file.write(r.text)
    # with open(file_path, 'r') as file:
    #     text = file.read()
    return file_path
