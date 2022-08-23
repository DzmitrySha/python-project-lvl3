"""Page loader - start module."""

import os
import requests
from page_loader import app_logger
from page_loader.processes import (make_soup, write_to_file)
from page_loader.download_sources import sources_download
from page_loader.download_html import html_download

logger = app_logger.get_logger(__name__)


def download(url: str, temp_folder=""):
    """Downloads and saves html page
    with local resources
    to exist specified folder"""
    output_path = os.path.join(os.getcwd(), temp_folder)

    logger.info(f"requested url: {url}")
    logger.info(f"output path: {output_path}")

    try:
        os.path.exists(output_path)
    except OSError as err:
        logger.error('the output directory does not exist!')
        raise err

    try:
        r = requests.get(url)
        r.raise_for_status()
    except (requests.exceptions.MissingSchema,
            requests.exceptions.InvalidSchema,
            requests.exceptions.InvalidURL) as error:
        logger.error('Requested url is not correct!')
        raise error
    except requests.exceptions.HTTPError as error:
        logger.error('HTTPError!')
        raise error
    except requests.exceptions.ConnectionError as error:
        logger.error('Connection Error!')
        raise error

    # except requests.exceptions.HTTPError as err:
    #     logger.error(f'Status code is not 200!: {err}')
    #     raise
    # except requests.exceptions.RequestException as err:
    #     logger.error(f'requested url is not correct!')
    #     raise

    soup = make_soup(url)
    html_file_path = html_download(soup, url, temp_folder)

    logger.info(f"write html file: {html_file_path} - download OK!")
    logger.info("downloading sources: ... ")

    sources_download(soup, url, temp_folder)
    write_to_file(html_file_path, soup.prettify())

    logger.info("All files successfully downloaded!")
    logger.info(f"page was downloaded as: {html_file_path}")

    return html_file_path
