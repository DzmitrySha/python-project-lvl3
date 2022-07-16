"""Processes module."""

import os
import re
import requests
from urllib.parse import urlparse, urljoin
from urllib.request import urlopen
from bs4 import BeautifulSoup


def make_soup(url: str) -> BeautifulSoup:
    """Make soup object from url"""
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


def write_txt_file(file_path, file_content):
    """Write html-content to file"""
    with open(file_path, 'w') as file:
        file.write(file_content)


def create_dir(dir_path: str):
    """Create directory if it not exists"""
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)


def write_bin_file(file_path, file_content):
    """Write binary source content to file"""
    with open(file_path, "wb") as file:
        file.write(file_content)


def has_scheme(url: str) -> bool:
    if urlparse(url).scheme:
        return True
    return False


def get_content(soup, url: str, tag: str, attr: str, dir_name, dir_path):
    domain_name = urlparse(url).netloc
    list_soup_tags = soup.find_all(tag)
    for src in list_soup_tags:
        if src is not None:
            src_url = src.get(attr)
            src_url_parse = urlparse(src_url)
            src_domain_name = str(src_url_parse.netloc)

            if domain_name in src_domain_name or not src_domain_name:
                if not src_domain_name:
                    src_url = urljoin(url, clearing_url(src_url))

                src_name = make_name(src_url, os.path.splitext(src_url)[1])
                src_local_url = os.path.join(dir_name, src_name)
                src_local_path = os.path.join(dir_path, src_name)
                src_content = requests.get(src_url).content

                write_bin_file(src_local_path, src_content)

                print(src)
                src[attr] = src[attr].replace(src.get(attr), src_local_url)
                print(src)
