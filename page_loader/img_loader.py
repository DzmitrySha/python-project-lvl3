"""Image loader module."""

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def make_dir(url, temp_folder=''):
    os.mkdir(url)
    pass


def img_download(url, temp_folder=''):
    soup = BeautifulSoup(url, 'html.parser')
    img_urls = soup.find_all('a')
    domain_name = urlparse(url).netloc

    for img_url in img_urls:
        if domain_name in img_url:
            r = requests.get(img_url)
            with open(img_url, "wb") as img:
                img.write(r.content)
    #         print(link.get('href'))
    # print(soup.prettify())
