"""Processes module."""

import os
import requests
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from page_loader.app_logger import make_logger

logger = make_logger(__name__)


def clearing_url(url: str) -> str:
    """Cut scheme and query from url"""
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
    """Write source content to file"""
    flag = 'wb' if isinstance(file_content, bytes) else 'w'
    with open(file_path, flag) as file:
        file.write(file_content)


def make_soup(url):
    try:
        response = requests.get(url)  # запрос на сервер
        response.raise_for_status()
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

    else:
        soup = BeautifulSoup(response.text, "html.parser")
    return soup
