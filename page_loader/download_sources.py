"""Sources downloader module."""

import os
from page_loader.processes import (make_name, create_dir, get_sources)

tags = {
    "img": "src",
    "link": "href",
    "script": "src",
}


def sources_download(soup, url: str, temp_folder=''):
    folder_name = make_name(url, ext="_files")
    folder_path = os.path.join(temp_folder, folder_name)
    create_dir(folder_path)

    for tag, attr in tags.items():
        get_sources(soup, url, tag, attr, folder_name, folder_path)
