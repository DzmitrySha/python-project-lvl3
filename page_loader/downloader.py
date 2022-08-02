"""Page loader - start module."""

import os
from page_loader import app_logger
from page_loader.processes import make_soup, write_to_file
from page_loader.download_sources import sources_download
from page_loader.download_html import html_download

logger = app_logger.get_logger(__name__)


def page_download(url: str, temp_folder=""):
    """Downloads and saves html page
    with local resources
    to exist specified folder"""
    logger.info(f"requested url: {url}")
    logger.info(f"output path: {os.path.join(os.getcwd(), temp_folder)}")

    soup = make_soup(url)
    html_file_path = html_download(soup, url, temp_folder)

    logger.info(f"write html file: {html_file_path}")
    logger.info("Downloading: ...")
    sources_download(soup, url, temp_folder)
    write_to_file(html_file_path, soup.prettify())

    logger.info(f"Page was downloaded as: {html_file_path}")

    return html_file_path
