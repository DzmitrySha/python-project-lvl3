"""HTML downloader module."""

import os
from page_loader.processes import make_name, write_to_file
from page_loader.app_logger import make_logger

logger = make_logger(__name__)


def html_download(soup, url: str, temp_folder=''):
    html_file_name = make_name(url, '.html')
    html_file_path = os.path.join(temp_folder, html_file_name)
    write_to_file(html_file_path, soup.prettify())  # запись в файл
    return html_file_name, html_file_path
