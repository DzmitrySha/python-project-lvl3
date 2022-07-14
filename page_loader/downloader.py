"""Page loader - start module."""

from page_loader.download_sources import sources_download
from page_loader.download_html import html_download


def page_download(url: str, temp_folder=""):
    """Downloads and saves html page
    with local resources
    to exist specified folder"""

    html_file_path = html_download(url, temp_folder)
    sources_download(url, temp_folder)

    return html_file_path
