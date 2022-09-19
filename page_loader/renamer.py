"""Transform url names to folder/file names
модуль для преобразования урлов в имена файлов/директорий
"""

import os
import re
from urllib.parse import urlparse, urljoin


def clearing_url(url: str) -> str:
    """Cut scheme and query from url"""
    parsed_url = urlparse(url)
    clear_url = parsed_url.netloc + parsed_url.path
    return clear_url


def make_name(url: str, ext='') -> str:
    """Make indent-name from url with specified extension."""
    indent = '-'
    mask = '[a-zA-Z0-9]'
    clear_url = clearing_url(url)
    extension = os.path.splitext(clear_url)[1]
    if extension == ext:
        clear_url = clear_url.replace(extension, '')
    name = "".join(char if re.match(mask, char) else indent
                   for char in clear_url)
    return name + ext if ext else name + '.html'


def make_path(source_url, url):
    """Make source path from source url."""
    dir_name = make_name(url, ext="_files")
    source_domain_name = urlparse(source_url).netloc

    if not source_domain_name:
        source_url = urljoin(url, clearing_url(source_url))

    source_ext = os.path.splitext(source_url)[1]
    source_file_name = make_name(source_url, source_ext)
    source_path_name = os.path.join(dir_name, source_file_name)
    return source_path_name
