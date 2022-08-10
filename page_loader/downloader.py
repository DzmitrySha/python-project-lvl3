"""Page loader - start module."""

import os
from page_loader import app_logger
from page_loader.processes import make_soup, write_to_file
from page_loader.download_sources import sources_download
from page_loader.download_html import html_download

logger = app_logger.get_logger(__name__)


def download(url: str, temp_folder=""):
    """Downloads and saves html page
    with local resources
    to exist specified folder"""
    logger.info(f"requested url: {url}")
    soup = make_soup(url)

    output_path = os.path.join(os.getcwd(), temp_folder)
    logger.info(f"output path: {output_path}")
    html_file_path = html_download(soup, url, temp_folder)

    logger.info(f"write html file: {html_file_path}")
    logger.info("downloading: ...")
    sources_download(soup, url, temp_folder)
    write_to_file(html_file_path, soup.prettify())

    logger.info(f"page was downloaded as: {html_file_path}")

    return html_file_path
