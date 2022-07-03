"""Image loader module."""

import os
import requests
from urllib.parse import urlparse
from page_loader.processes import make_soup, make_name, write_to_file


def page_download(url: str, temp_folder=""):
    """Downloads and saves html page with images to exist specified folder"""

    # директория и путь для хранения файлов
    dir_name = make_name(url, ext="_files")
    dir_path = os.path.join(temp_folder, dir_name)

    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    # создаем объект Beautifulsoup
    soup = make_soup(url)
    # собираем все строки с тегом img из исходного url
    img_tags = soup.find_all('img')

    for tag in img_tags:
        img_url = tag.get('src')
        if urlparse(img_url).netloc:
            file_name = make_name(img_url, os.path.splitext(img_url)[1])
            html_file_path = os.path.join(dir_path, file_name)

            req = requests.get(img_url)
            with open(html_file_path, "wb") as file:
                file.write(req.content)

            for img in img_tags:
                img['src'] = img['src'].replace(img_url, html_file_path)

    # имя html-файла
    html_file_name = make_name(url, ext=".html")
    # путь к сохранению html-файла
    html_file_path = os.path.join(temp_folder, html_file_name)
    # сохранение html-файла с измененными ссылками на файлы картинок
    write_to_file(html_file_path, soup.prettify())
    return html_file_path
