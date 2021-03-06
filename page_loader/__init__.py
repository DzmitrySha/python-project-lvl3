"""
Page Loader - Downloads a page from the internet to the specified folder.

Dzmitry Shapavalau: [https://github.com/DzmitrySha]
This project: [https://github.com/DzmitrySha/python-project-lvl3]

"""

from page_loader.downloader import page_download            # noqa: F401
from page_loader.processes import (make_soup, make_name,    # noqa: F401
                                   create_dir,              # noqa: F401
                                   get_content,             # noqa: F401
                                   write_txt_file,          # noqa: F401
                                   write_bin_file)          # noqa: F401
