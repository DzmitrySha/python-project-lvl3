"""HTML loader module."""

import os
from page_loader.processes import make_name, html_parser, write_to_file


def html_download(url: str, temp_folder='') -> str:
    """Download html page, save to exist specified folder."""
    html = html_parser(url)

    filename = make_name(url, ext=".html")
    file_path = os.path.join(temp_folder, filename)

    write_to_file(file_path, html[1])
    return file_path
