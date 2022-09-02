"""Test sources downloader"""

import os
import pytest
import tempfile
from bs4 import BeautifulSoup
from page_loader.download_sources import sources_download


HTML_MAIN_URL = "https://ru.hexlet.io"
PAGE_URL = "https://ru.hexlet.io/courses"
JPG_URL = "https://ru.hexlet.io/assets/professions/python.jpg"
CSS_URL = "https://ru.hexlet.io/assets/application.css"
JS_URL = "https://ru.hexlet.io/packs/js/runtime.js"

DIR_NAME = "ru-hexlet-io_files"
FILENAMES = {
    "page_url_name": "ru-hexlet-io-courses",
    "jpg_mock": "ru-hexlet-io-assets-professions-python.jpg",
    "css_mock": "ru-hexlet-io-assets-application.css",
    "js_mock": "ru-hexlet-io-packs-js-runtime.js",
}


def read_file(path: str, flag='r'):
    with open(path, flag) as file:
        return file.read()


@pytest.mark.asyncio
async def test_sources_download(before_html_path, jpg_file_path,
                                css_file_path, js_file_path,
                                result_html_path, urls,
                                requests_mock):
    before_html_mock = read_file(before_html_path)
    result_html_mock = read_file(result_html_path)
    jpg_mock = read_file(jpg_file_path, 'rb')
    css_mock = read_file(css_file_path)
    js_mock = read_file(js_file_path, 'rb')

    requests_mock.get(HTML_MAIN_URL, text=result_html_mock)
    requests_mock.get(PAGE_URL, text=before_html_mock)
    requests_mock.get(JPG_URL, content=jpg_mock)
    requests_mock.get(CSS_URL, text=css_mock)
    requests_mock.get(JS_URL, content=js_mock)

    soup = BeautifulSoup(before_html_mock, "html.parser")

    with tempfile.TemporaryDirectory() as tmpdirname:
        sources_download(soup, HTML_MAIN_URL, tmpdirname)
        for file_name in FILENAMES.values():
            file_path = os.path.join(DIR_NAME, file_name)
            assert os.path.exists(os.path.join(tmpdirname, file_path))
