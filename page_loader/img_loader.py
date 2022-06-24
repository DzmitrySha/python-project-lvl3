"""Image loader module."""

from bs4 import BeautifulSoup


def img_download(url, temp_folder=''):
    soup = BeautifulSoup(url, 'html.parser')
    print(soup.prettify())
