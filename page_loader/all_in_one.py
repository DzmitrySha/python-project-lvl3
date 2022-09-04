""" all in one """

import os
import sys
import requests
import re
from app_logger import make_logger
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from progress.bar import FillingCirclesBar


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
    """Write binary source content to file"""
    fmt = 'wb' if isinstance(file_content, bytes) else 'w'
    with open(file_path, fmt) as file:
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
    else:
        soup = BeautifulSoup(response.text, "html.parser")
    return soup


def get_sources_urls(soup):
    list_sources_urls = []
    list_soup_tags = soup.find_all(list(tags.keys()))
    for src in list_soup_tags:
        for attr in set(tags.values()):
            list_sources_urls.append(src.get(attr))
    list_sources_urls = list(filter(lambda x: x is not None, list_sources_urls))
    return list_sources_urls


def replace_urls(soup, diff_urls):
    for pair in diff_urls:
        if soup.find(href=pair['old_url']):
            sfind = soup.find(href=pair['old_url'])
            sfind['href'] = sfind['href'].replace(
                pair['old_url'], pair['new_url'])
        if soup.find(src=pair['old_url']):
            sfind = soup.find(src=pair['old_url'])
            sfind['src'] = sfind['src'].replace(
                pair['old_url'], pair['new_url'])


def sources_download(soup, url: str, temp_folder: str):
    """Get sources from HTML page"""

    dir_name = make_name(url, ext="_files")
    dir_path = os.path.join(temp_folder, dir_name)
    create_dir(dir_path)

    domain_name = urlparse(url).netloc
    diff_urls = []
    list_sources_urls = get_sources_urls(soup)

    for src_url in list_sources_urls:
        # print(src_url)
        src_raw_url = src_url

        src_domain_name = urlparse(src_url).netloc
        if not src_domain_name:
            src_url = urljoin(url, clearing_url(src_url))

        if domain_name in src_url:
            src_ext = os.path.splitext(src_url)[1]
            src_name = make_name(src_url, src_ext)

            src_local_url = os.path.join(dir_name, src_name)
            src_local_path = os.path.join(dir_path, src_name)

            src_content = requests.get(src_url).content  # запрос на сервер

            bar = FillingCirclesBar(f'{src_name} ', min=0, max=1)

            bar.next()
            write_to_file(src_local_path, src_content)  # запись в файл
            logger.info(f"{src_name} - download OK!")
            bar.finish()

            diff_urls.append({'old_url': src_raw_url, 'new_url': src_local_url})
    replace_urls(soup, diff_urls)


def html_download(soup, url: str, temp_folder=''):
    html_file_name = make_name(url, '.html')
    html_file_path = os.path.join(temp_folder, html_file_name)
    write_to_file(html_file_path, soup.prettify())  # запись в файл
    return html_file_name


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
    sources_download(soup, url, temp_folder)
    html_file_name = html_download(soup, url, temp_folder)

    return html_file_name


if __name__ == "__main__":
    source_url = 'https://page-loader.hexlet.repl.co'
    output = 'var/tmp/'

    tags = {
        "img": "src",
        "link": "href",
        "script": "src",
    }

    output_path = os.path.join(os.getcwd(), output)
    print(f"requested url: {source_url}")
    print(f"output folder: {output_path}")

    try:
        html_file_path = download(sys.argv[1], sys.argv[2])
        print(f"page was downloaded as: {html_file_path}")
    except Exception as error:
        logger.debug(error)
        print("An unexpected error occurred.\n"
              "See log file for details (page_loader.log).")
        sys.exit(1)
