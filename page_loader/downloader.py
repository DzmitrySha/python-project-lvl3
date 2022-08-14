"""Page loader - start module."""

import os
# import sys
import requests

from page_loader import app_logger
from page_loader.processes import (make_soup, write_to_file,
                                   is_folder_exists)
from page_loader.download_sources import sources_download
from page_loader.download_html import html_download

logger = app_logger.get_logger(__name__)


def download(url: str, temp_folder=""):
    """Downloads and saves html page
    with local resources
    to exist specified folder"""
    output_path = os.path.join(os.getcwd(), temp_folder)

    try:
        is_folder_exists(output_path)
    except OSError as error:
        logger.info(
            'the output directory does not exist! Please create it before!'
        )
        raise error

    logger.info(f"requested url: {url}")
    logger.info(f"output path: {output_path}")

    try:
        requests.get(url)
    except requests.exceptions.RequestException as error:
        logger.error('requested url is not correct!')
        raise error

    soup = make_soup(url)
    html_file_path = html_download(soup, url, temp_folder)

    logger.info(f"write html file: {html_file_path}")
    logger.info("downloading sources: ... ")

    sources_download(soup, url, temp_folder)
    write_to_file(html_file_path, soup.prettify())

    logger.info(f"page was downloaded as: {html_file_path}")

    return html_file_path
    # sys.exit(1)
