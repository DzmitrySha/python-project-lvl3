"""Processes module."""

import os
import sys
import requests
import re
from urllib.request import urlopen
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from progress.bar import ChargingBar
from page_loader import app_logger

logger = app_logger.get_logger(__name__)


def is_url_correct(url: str):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        logger.error('requested url is not correct!')
        sys.exit(1)
    return True


def is_folder_exists(folder_path: str) -> bool:
    if not os.path.exists(folder_path):
        logger.error('the output folder does not exist! '
                     'Please, create it before!')
        sys.exit(1)
    return True


def make_soup(url: str) -> BeautifulSoup:
    """Make soup object from url"""
    if is_url_correct(url):
        soup = BeautifulSoup(urlopen(url), 'html.parser')
        return soup


def clearing_url(url: str) -> str:
    """Make URL clean, cut scheme and query"""
    parsed_url = urlparse(url)
    clear_url = parsed_url.netloc + parsed_url.path
    return clear_url


def make_name(url: str, ext='') -> str:
    """Make indent-name from url with specified extension."""
    indent = '-'
    mask = '[a-zA-Z0-9]'
    clear_url = clearing_url(url)
    extension = os.path.splitext(clear_url)[1]
    if extension == ext:
        clear_url = clear_url.replace(extension, '')
    name = "".join(char if re.match(mask, char) else indent
                   for char in clear_url)
    return name + ext if ext else name


def create_dir(dir_path: str):
    """Create directory if it not exists"""
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)


def write_to_file(file_path, file_content):
    """Write binary source content to file"""
    fmt = 'wb' if isinstance(file_content, bytes) else 'w'
    with open(file_path, fmt) as file:
        file.write(file_content)


def get_sources(soup, url: str, tag: str, attr: str,
                dir_name: str, dir_path: str):
    """Get sources from HTML page"""
    domain_name = urlparse(url).netloc
    list_soup_tags = soup.find_all(tag)
    for src in list_soup_tags:
        if src:
            src_url = src.get(attr)
            src_domain_name = str(urlparse(src_url).netloc)

            if domain_name in src_domain_name or not src_domain_name:
                if not src_domain_name:

                    src_url = urljoin(url, clearing_url(src_url))

                src_name = make_name(src_url, os.path.splitext(src_url)[1])
                src_local_url = os.path.join(dir_name, src_name)
                src_local_path = os.path.join(dir_path, src_name)
                src_content = requests.get(src_url).content

                bar = ChargingBar('Processing', max=100)
                logger.info(f" source url: {src_url}")
                for i in range(100):
                    bar.next()
                write_to_file(src_local_path, src_content)

                src[attr] = src[attr].replace(src.get(attr), src_local_url)

                bar.finish()
