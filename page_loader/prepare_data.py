"""Processing/prepare html and data for download resources module
Модуль для обработки/подготовки html и собирания ресурсов
"""

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from page_loader.app_logger import make_logger
from page_loader.in_out import write_to_file
from page_loader.renamer import make_name, make_path

logger = make_logger(__name__)

tags = {
    "img": "src",
    "link": "href",
    "script": "src",
}


def make_soup(url) -> BeautifulSoup:
    try:
        response = requests.get(url)
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

    else:
        soup = BeautifulSoup(response.text, "html.parser")
    return soup


def get_resources_urls(soup: BeautifulSoup, url: str) -> list:
    resources_urls = []
    domain_name = urlparse(url).netloc
    soup_tags = soup.find_all(tags.keys())

    for src in soup_tags:
        for attr in set(tags.values()):
            resources_urls.append(src.get(attr))

    resources_urls = filter(lambda x: x is not None and                 # noqa W504
        (urlparse(x).netloc == domain_name or not urlparse(x).netloc),  # noqa E128
        resources_urls
    )
    resources_urls_paths = list((src_url, make_path(src_url, url))
                                for src_url in resources_urls if resources_urls)
    return resources_urls_paths


def replace_urls(soup: BeautifulSoup, urls_paths: list):
    for url, path in urls_paths:
        if soup.find(href=url):
            sfind = soup.find(href=url)
            sfind['href'] = sfind['href'].replace(url, path)
        if soup.find(src=url):
            sfind = soup.find(src=url)
            sfind['src'] = sfind['src'].replace(url, path)


def prepare_resources(url: str, temp_folder=""):
    soup = make_soup(url)
    resources_urls_paths = get_resources_urls(soup, url)

    replace_urls(soup, resources_urls_paths)
    html_file_path = os.path.join(temp_folder, make_name(url))
    write_to_file(html_file_path, soup.prettify())

    return resources_urls_paths, html_file_path
