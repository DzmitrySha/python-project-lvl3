"""Naming module"""

import os
import re
from urllib.parse import urlparse


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
    if extension:
        clear_url = clear_url.replace(extension, '')
    indent_name = "".join(char if re.match(mask, char) else indent
                          for char in clear_url)
    return indent_name + ext if ext else indent_name
