"""
Page Loader - Downloads a page from the internet to the specified folder.

Dzmitry Shapavalau: [https://github.com/DzmitrySha]
This project: [https://github.com/DzmitrySha/python-project-lvl3]

"""

from page_loader.downloader import download                     # noqa: F401
from page_loader.in_out import create_dir, write_to_file        # noqa: F401
from page_loader.renamer import (clearing_url, make_name,       # noqa: F401
                                 make_path)              # noqa: F401
