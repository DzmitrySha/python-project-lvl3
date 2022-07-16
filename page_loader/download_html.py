"""HTML downloader module."""

import os
from page_loader.processes import (make_name, write_txt_file)


def html_download(soup, url: str, temp_folder='') -> str:
    html_file_name = make_name(url, ".html")
    html_file_path = os.path.join(temp_folder, html_file_name)
    html_content = soup.prettify()

    write_txt_file(html_file_path, html_content)
    return html_file_path
