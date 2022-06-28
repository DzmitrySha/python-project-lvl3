"""Image loader module."""

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from page_loader.naming import make_name


def make_dir(url):
    temp_folder = make_name(url, ext="_files")
    os.mkdir(temp_folder)
    return temp_folder


def files_download(url):
    soup = BeautifulSoup(url, 'html.parser')
    files_urls = soup.find_all('a')
    domain_name = urlparse(url).netloc

    for file_url in files_urls:
        if domain_name in (file_url, ""):
            r = requests.get(file_url)
            with open(file_url, "wb") as file:
                file.write(r.content)
    #         print(link.get('href'))
    # print(soup.prettify())
