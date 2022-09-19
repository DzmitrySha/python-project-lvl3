"""Main downloader module (downloader.py)"""

import os
from page_loader import app_logger
from page_loader.prepare_data import prepare_resources
from page_loader.resources import download_resources

logger = app_logger.make_logger(__name__)


def download(url: str, temp_folder=''):

    output_path = os.path.join(os.getcwd(), temp_folder)

    logger.info(f"Requested url: {url}")
    logger.info(f"Output path: {output_path}")
    resources_urls_paths, html_file_path = prepare_resources(url, temp_folder)

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

    logger.info("Downloading resources: ... ")
    download_resources(resources_urls_paths, url, temp_folder)
    logger.info("All resources successfully downloaded!")
    logger.info(f"Page was downloaded as: '{html_file_path}'")

    return html_file_path
