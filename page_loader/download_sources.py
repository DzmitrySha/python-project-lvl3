"""IMG downloader module."""

import os
from page_loader.processes import (make_name, create_dir, get_content)

tags = {
    "img": "src",
    "link": "href",
    "script": "src",
}


def sources_download(soup, url: str, temp_folder=''):
    dir_name = make_name(url, ext="_files")
    dir_path = os.path.join(temp_folder, dir_name)
    create_dir(dir_path)

    for tag, attr in tags.items():
        get_content(soup, url, tag, attr, dir_name, dir_path)
