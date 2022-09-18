"""Processing/prepare html and data for download resources module
Модуль для обработки/подготовки html и собирания ресурсов
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from page_loader.app_logger import make_logger
from page_loader.renamer import make_name

logger = make_logger(__name__)

tags = {
    "img": "src",
    "link": "href",
    "script": "src",
}


def make_soup(url) -> BeautifulSoup:
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

    else:
        soup = BeautifulSoup(response.text, "html.parser")
    return soup


def prepare_resources_urls(soup: BeautifulSoup, url: str) -> list:
    resources_urls = []
    domain_name = urlparse(url).netloc
    soup_tags = soup.find_all(tags.keys())

    for src in soup_tags:
        for attr in set(tags.values()):
            resources_urls.append(src.get(attr))

    resources_urls = filter(lambda x: x is not None, resources_urls)
    resources_urls = filter(
        lambda x: urlparse(x).netloc == domain_name or not urlparse(x).netloc,
        resources_urls)
    resources_urls_paths = list((url, make_name(url)) for url in resources_urls)

    return resources_urls_paths


# def replace_urls(soup, diff_urls: list):
#     for pair in diff_urls:
#         if soup.find(href=pair['old_url']):
#             sfind = soup.find(href=pair['old_url'])
#             sfind['href'] = sfind['href'].replace(
#                 pair['old_url'], pair['new_url'])
#         if soup.find(src=pair['old_url']):
#             sfind = soup.find(src=pair['old_url'])
#             sfind['src'] = sfind['src'].replace(
#                 pair['old_url'], pair['new_url'])


def prepare_resources(url: str):
    soup = make_soup(url)
    resources = prepare_resources_urls(soup, url)
    html_file_path = make_name(url)
    return resources, html_file_path


print(prepare_resources("https://page-loader.hexlet.repl.co"))
