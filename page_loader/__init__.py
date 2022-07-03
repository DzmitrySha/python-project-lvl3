"""
Page Loader - Downloads a page from the internet to the specified folder.

Dzmitry Shapavalau: [https://github.com/DzmitrySha]
This project: [https://github.com/DzmitrySha/python-project-lvl3]

"""

from page_loader.html_loader import html_download           # noqa: F401
from page_loader.files_loader import files_download         # noqa: F401
from page_loader.processes import (html_parser, make_name,  # noqa: F401
                                   write_to_file)           # noqa: F401
