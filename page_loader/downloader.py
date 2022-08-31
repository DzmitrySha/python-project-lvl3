"""Page loader - start module."""

import os
from page_loader import app_logger
from page_loader.processes import make_soup
from page_loader.download_sources import sources_download
from page_loader.download_html import html_download

logger = app_logger.make_logger(__name__)


def download(url: str, temp_folder=''):

    output_path = os.path.join(os.getcwd(), temp_folder)

    logger.info(f"requested url: {url}")
    logger.info(f"output path: {output_path}")

    try:
        os.path.exists(output_path)
    except FileNotFoundError as err:
        logger.error('The specified folder does not exist!')
        raise err
    except PermissionError as err:
        logger.error('You don`t have permission to write in this folder!')
        raise err
    except OSError as err:
        logger.error('Something wrong with the output path!...')
        raise err

    soup = make_soup(url)
    logger.info("downloading sources: ... ")
    sources_download(soup, url, temp_folder)
    logger.info("All sources successfully downloaded!")

    html_file_name, html_file_path = html_download(soup, url, temp_folder)
    logger.info(f"write html file: {html_file_path} - download OK!")
    logger.info(f"page was downloaded as: {html_file_path}")

    return html_file_name
