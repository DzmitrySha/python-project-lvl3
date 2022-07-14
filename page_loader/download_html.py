"""HTML downloader module."""

from page_loader.processes import (make_soup, make_name,
                                   make_html_file_path, write_txt_file)


def html_download(url: str, temp_folder='') -> str:
    html_content = make_soup(url).prettify()
    html_file_name = make_name(url, ".html")
    html_file_path = make_html_file_path(html_file_name, temp_folder)
    write_txt_file(html_file_path, html_content)
    return html_file_path
