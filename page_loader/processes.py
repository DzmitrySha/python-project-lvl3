"""Processes module."""

import os
import re
import requests
from urllib.parse import urlparse, urljoin
from urllib.request import urlopen
from bs4 import BeautifulSoup


def make_soup(url: str) -> BeautifulSoup:
    """Make soup object from url"""
    soup = BeautifulSoup(urlopen(url), 'html.parser')
    return soup


def clearing_url(url: str) -> str:
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


def make_html_file_path(html_file_name, temp_folder='') -> str:
    """Make html file path"""
    # html_file_name = make_name(url, ext=".html")
    html_file_path = os.path.join(temp_folder, html_file_name)
    return html_file_path


def write_html_file(html_file_path, html_content):
    """Write html-content to file"""
    with open(html_file_path, 'w') as file:
        file.write(html_content)


def make_dir_path(dir_name, temp_folder='') -> str:
    """Make directory path"""
    # dir_name = make_name(url, ext="_files")
    dir_path = os.path.join(temp_folder, dir_name)
    return dir_path


def create_dir(dir_path: str):
    """Create directory if it not exists"""
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)


def write_bin_file(file_path, file_content):
    """Write binary source content to file"""
    with open(file_path, "wb") as file:
        file.write(file_content)


def write_files(soup: BeautifulSoup,
                url: str,
                tag: str,
                attr: str,
                dir_path: str):
    # доменное имя
    domain_name = urlparse(url).netloc
    # собираем список строк с тегами tags из объекта soup
    list_tags = soup.find_all(tag)

    for line in list_tags:
        # для каждой строки из списка берём значение его аттрибута
        line_url = clearing_url(line.get(attr))
        line_domain_name = urlparse(line_url).netloc

        # если ссылка на файл содержит доменное имя или не содержит его вообще,
        # то скачиваем файл
        if domain_name in line_domain_name or not line_domain_name:
            # формируем ссылку на файл, если она не содержит схему и домен
            if not line_domain_name:
                line_url = urljoin(url, line_url)

            # формируем имя файла и локальный путь к нему
            source_name = make_name(line_url, os.path.splitext(line_url)[1])
            local_path = os.path.join(dir_path, source_name)
            content = requests.get(line_url).content

            write_bin_file(local_path, content)

            # заменяем ссылки на локальные пути к файлам
            for source in list_tags:
                source[attr] = source[attr].replace(line_url, local_path)
