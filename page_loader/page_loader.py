"""Page loader - main module."""

from page_loader.html_loader import html_download
from page_loader.img_loader import img_download


def download(url: str, temp_folder=''):
    """Start download."""
    img_download(url, temp_folder)
    html_path = html_download(url, temp_folder)
    return html_path
