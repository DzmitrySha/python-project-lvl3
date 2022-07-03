"""Processes module."""

import os
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.request import urlopen


def make_soup(url: str) -> BeautifulSoup:
    soup = BeautifulSoup(urlopen(url), 'html.parser')
    return soup


def clearing_(url: str) -> str:
    url_parse = urlparse(url)
    url_netloc = url_parse.netloc
    url_path = url_parse.path
    clear_url = url_netloc + url_path
    return clear_url


def make_name(url: str, ext='') -> str:
    """Make indent-name with extension from url."""
    indent = '-'
    mask = '[a-zA-Z0-9]'
    clear_url = clearing_(url)
    extension = os.path.splitext(clear_url)[1]
    if extension == ext:
        clear_url = clear_url.replace(extension, '')
    indent_name = "".join(char if re.match(mask, char) else indent
                          for char in clear_url)
    return indent_name + ext if ext else indent_name


def write_to_file(file_path: str, text: str):
    """Write text to file."""
    with open(file_path, 'w') as file:
        file.write(text)
