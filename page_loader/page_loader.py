"""Page loader - main module."""

from page_loader.html_loader import html_download
from page_loader.files_loader import files_download


def download(url: str, temp_folder=''):
    """Start download."""
    html_path = html_download(url, temp_folder)
    files_download(url, temp_folder)
    return html_path
