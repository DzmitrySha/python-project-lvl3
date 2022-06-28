"""Naming module"""

import os
import re
from urllib.parse import urlparse


def make_indent_name_(url):
    """Make file-name from file.name"""
    indent = '-'
    mask = '[a-zA-Z0-9]'
    url_scheme = f"{urlparse(url).scheme}://"
    cut_url = url.replace(url_scheme, '', 1)
    indent_name = "".join(char if re.match(mask, char) else indent
                          for char in cut_url)
    return indent_name


def make_name(url: str, ext='') -> str:
    """Make indent-name with extension or  from url."""
    indent_name = make_indent_name_(url)
    return indent_name + ext if os.path.splitext(url)[1] != ext else indent_name
