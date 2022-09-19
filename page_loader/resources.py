"""Downloading resources from prepared urls list module"""
import os.path

import requests
from urllib.parse import urlparse, urljoin
from progress.bar import Bar
from page_loader.in_out import create_dir, write_to_file
from page_loader.renamer import make_name
from page_loader import app_logger

logger = app_logger.make_logger(__name__)


def download_resources(resources_urls_paths: list, url: str, temp_folder):
    """Get sources from HTML page"""

    if resources_urls_paths:
        dir_path = os.path.join(temp_folder, make_name(url, "_files"))
        create_dir(dir_path)

    bar = Bar('Downloading resources: ', max=len(resources_urls_paths))

    for src_url, path in resources_urls_paths:
        src_domain_name = urlparse(src_url).netloc
        if not src_domain_name:
            src_url = urljoin(url, src_url)

        bar.next()
        try:
            response = requests.get(src_url)
            src_content = response.content
        except requests.exceptions.RequestException:
            logger.error('Connection Error while downloading resources!')
            continue

        file_path = os.path.join(temp_folder, path)
        write_to_file(file_path, src_content)
        logger.info(f"{file_path} - download OK!")

    bar.finish()
