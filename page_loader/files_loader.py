"""Image loader module."""

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from page_loader.naming import make_name


def write_to_file(file_path: str, text: str):
    """Write text to file."""
    with open(file_path, 'w') as file:
        file.write(text)


def files_download(url: str, temp_folder=""):
    soup = BeautifulSoup(url, 'html.parser')
    files_urls = soup.find_all('a')
    domain_name = urlparse(url).netloc

    dir_path = os.path.join(temp_folder, make_name(url, ext="_files"))
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    os.chdir(dir_path)

    for file_url in files_urls:
        if domain_name in (file_url, ""):
            r = requests.get(file_url)
            with open(file_url, "wb") as file:
                file.write(r.content)
    #         print(link.get('href'))
    # print(soup.prettify())
