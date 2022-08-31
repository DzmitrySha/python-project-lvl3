"""
Page Loader - Downloads a page from the internet to the specified folder.

Dzmitry Shapavalau: [https://github.com/DzmitrySha]
This project: [https://github.com/DzmitrySha/python-project-lvl3]

"""

from page_loader.downloader import download                 # noqa: F401
from page_loader.processes import (make_soup,               # noqa: F401
                                   make_name,               # noqa: F401
                                   clearing_url,            # noqa: F401
                                   create_dir,              # noqa: F401
                                   write_to_file)           # noqa: F401
