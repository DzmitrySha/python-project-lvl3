"""Page loader - main module."""

from page_loader.downloader import page_download


def download(url: str, temp_folder=''):
    """Start download."""
    html_path = page_download(url, temp_folder)
    return html_path
