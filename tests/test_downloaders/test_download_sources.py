"""Test sources downloader"""

import pytest
import requests
import tempfile
from bs4 import BeautifulSoup
from page_loader.download_sources import sources_download

DOWNLOADER = 'download_sources'


def read_file(path: str, flag='r'):
    with open(path, flag) as file:
        return file.read()


@pytest.mark.asyncio
async def test_sources_download(before_html, jpg_file,
                                css_file, js_file,
                                requests_mock):

    soup = BeautifulSoup(read_file(before_html), "html.parser")
    jpg_mock = read_file(jpg_file, 'rb')
    css_mock = read_file(css_file)
    js_mock = read_file(js_file, 'rb')

    requests_mock.get(
        "https://ru.hexlet.io/assets/professions/python.jpg", content=jpg_mock)
    jpg_mock = requests.get(
        "https://ru.hexlet.io/assets/professions/python.jpg", jpg_file).content

    requests_mock.get(
        "https://ru.hexlet.io/assets/application.css", text=css_mock)
    css_mock = requests.get(
        "https://ru.hexlet.io/assets/application.css", css_file).text

    requests_mock.get(
        "https://ru.hexlet.io/packs/js/runtime.js", content=js_mock)
    js_mock = requests.get(
        "https://ru.hexlet.io/packs/js/runtime.js", js_file).content

    requests_mock.get(
        "https://ru.hexlet.io/courses", text=before_html)
    html_mock = requests.get("https://ru.hexlet.io/courses", before_html).text

    with tempfile.TemporaryDirectory() as tmpdirname:
        sources_download(
            soup=soup,
            url="https://ru.hexlet.io/courses",
            temp_folder=tmpdirname
        )

        # assert os.path.exists(jpg_mock)
        # assert os.path.exists(css_mock)
        # assert os.path.exists(js_mock)
        # assert os.path.exists(html_mock)


        # assert jpg_mock == jpg_after_func
        # assert css_mock == css_after_func
        # assert js_mock == js_after_func

        # assert jpg_mock == jpg_after_func
        # assert css_mock == css_after_func
        # assert js_mock == js_after_func