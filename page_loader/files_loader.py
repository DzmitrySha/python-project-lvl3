"""Image loader module."""

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.request import urlopen
from page_loader.naming import make_name


def write_to_file(file_path: str, text: str):
    """Write text to file."""
    with open(file_path, 'w') as file:
        file.write(text)


def files_download(url: str, temp_folder=""):
    # директория и путь для хранения файлов
    dir_name = make_name(url, ext="_files")
    dir_path = os.path.join(temp_folder, dir_name)

    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    domain_name = urlparse(url).netloc

    # все ссылки из url
    soup = BeautifulSoup(urlopen(url), 'html.parser')
    all_urls = soup.find_all('img')
    # имя домена
    domain_name = urlparse(url).netloc

    for link in all_urls:
        file_url = link.get('src')
        if urlparse(file_url).netloc:
            file_name = make_name(file_url, os.path.splitext(file_url)[1])
            file_path = os.path.join(dir_path, file_name)

            req = requests.get(file_url)
            with open(file_path, "wb") as file:
                file.write(req.content)
