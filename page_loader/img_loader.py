"""Image loader module."""

import os
from bs4 import BeautifulSoup


def make_dir(url, temp_folder=''):
    os.mkdir(url)
    pass


def img_download(url, temp_folder=''):
    soup = BeautifulSoup(url, 'html.parser')
    img_links = soup.find_all('a')
    for link in img_links:
        print(link.get('href'))
    print(soup.prettify())
