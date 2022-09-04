"""Sources downloader module."""

import os
import requests
from urllib.parse import urlparse, urljoin
from progress.bar import Bar
from page_loader.processes import (make_name, create_dir,
                                   clearing_url, write_to_file)
from page_loader.app_logger import make_logger

logger = make_logger(__name__)

tags = {
    "img": "src",
    "link": "href",
    "script": "src",
}


def prepare_sources_urls(soup, url: str) -> list:
    list_sources_urls = []
    domain_name = urlparse(url).netloc
    list_soup_tags = soup.find_all(list(tags.keys()))
    for src in list_soup_tags:
        for attr in set(tags.values()):
            list_sources_urls.append(src.get(attr))
    pre_url_list = filter(lambda x: x is not None, list_sources_urls)
    list_sources_urls = list(filter(
        lambda x: urlparse(x).netloc == domain_name
        or not urlparse(x).netloc, pre_url_list)
    )
    print(list_sources_urls)
    return list_sources_urls


def replace_urls(soup, diff_urls: list):
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

    diff_urls = []
    list_sources_urls = prepare_sources_urls(soup, url)
    bar = Bar('Downloading: ', max=len(list_sources_urls))

    for src_url in list_sources_urls:
        src_raw_url = src_url
        src_domain_name = urlparse(src_url).netloc

        if not src_domain_name:
            src_url = urljoin(url, clearing_url(src_url))

        src_ext = os.path.splitext(src_url)[1]
        src_name = make_name(src_url, src_ext)

        src_local_url = os.path.join(dir_name, src_name)
        src_local_path = os.path.join(dir_path, src_name)

        bar.next()

        try:
            response = requests.get(src_url)
            src_content = response.content
        except requests.exceptions.RequestException:
            logger.error('Connection Error while downloading resources!')
            continue
        write_to_file(src_local_path, src_content)  # запись в файл
        logger.info(f"{src_name} - download OK!")
        diff_urls.append({'old_url': src_raw_url, 'new_url': src_local_url})
    replace_urls(soup, diff_urls)

    bar.finish()
