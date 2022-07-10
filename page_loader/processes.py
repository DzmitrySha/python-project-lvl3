"""Processes module."""

import os
import re
import requests
from urllib.parse import urlparse, urljoin
from urllib.request import urlopen
from bs4 import BeautifulSoup


def make_soup(url: str) -> BeautifulSoup:
    soup = BeautifulSoup(urlopen(url), 'html.parser')
    return soup


def clearing_url(url: str) -> str:
    url_parse = urlparse(url)
    url_netloc = url_parse.netloc
    url_path = url_parse.path
    clear_url = url_netloc + url_path
    return clear_url


def make_name(url: str, ext='') -> str:
    """Make indent-name with extension from url."""
    indent = '-'
    mask = '[a-zA-Z0-9]'
    clear_url = clearing_url(url)
    extension = os.path.splitext(clear_url)[1]
    if extension == ext:
        clear_url = clear_url.replace(extension, '')
    indent_name = "".join(char if re.match(mask, char) else indent
                          for char in clear_url)
    return indent_name + ext if ext else indent_name


def make_dir_path(url: str, temp_folder='') -> str:
    # директория и путь для хранения файлов
    dir_name = make_name(url, ext="_files")
    dir_path = os.path.join(temp_folder, dir_name)
    # если директории не существует, то создаём её
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    return dir_path


def write_html_file(soup: BeautifulSoup, url: str, temp_folder='') -> str:
    # имя html-файла
    html_file_name = make_name(url, ext=".html")
    # путь к сохранению html-файла
    html_file_path = os.path.join(temp_folder, html_file_name)
    # сохранение html-файла с измененными ссылками на файлы картинок
    with open(html_file_path, 'w') as file:
        file.write(soup.prettify())
    return html_file_path


def write_source_file(source_url, local_path):
    """Write source content to file"""
    # считываем и записываем контент, содержащийся в картинке в файл
    req = requests.get(source_url)
    with open(local_path, "wb") as file:
        file.write(req.content)


def write_bin_files(soup: BeautifulSoup,
                    url: str,
                    tags: str,
                    attr: str,
                    dir_path: str):
    # собираем все строки с тегом img из объекта soup (html файла)
    source_tags = soup.find_all(tags)
    # выделяем из url доменное имя
    domain_name = urlparse(url).netloc

    for tag in source_tags:
        # из каждого тега img берём аттрибут src
        source_url = tag.get(attr)
        source_domain_name = urlparse(source_url).netloc

        # если src содержит доменное имя или не содержит его вообще,
        # то скачиваем файл
        if not source_domain_name or domain_name in source_domain_name:
            # если ссылка на файл не содержит схему и доменное имя,
            # добавляем их в ссылку
            if not source_domain_name:
                source_url = urljoin(url, source_url)

            # формируем имя файла и локальный путь к нему
            source_name = make_name(source_url, os.path.splitext(source_url)[1])
            local_path = os.path.join(dir_path, source_name)

            write_source_file(source_url, local_path)

            # заменяем ссылки на локальные пути к файлам
            for source in source_tags:
                source[attr] = source[attr].replace(source_url, local_path)
