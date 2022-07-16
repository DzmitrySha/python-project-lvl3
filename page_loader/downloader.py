"""Page loader - start module."""

from page_loader.processes import make_soup
from page_loader.download_sources import sources_download
from page_loader.download_html import html_download


def page_download(url: str, temp_folder=""):
    """Downloads and saves html page
    with local resources
    to exist specified folder"""

    soup = make_soup(url)

    sources_download(soup, url, temp_folder)
    html_file_path = html_download(soup, url, temp_folder)

    return html_file_path
