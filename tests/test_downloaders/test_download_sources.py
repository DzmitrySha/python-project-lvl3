"""Test sources downloader"""

import pytest
import requests
import tempfile
from bs4 import BeautifulSoup
from page_loader.download_sources import sources_download

DOWNLOADER = 'download_sources'


@pytest.mark.asyncio
async def test_sources_download(before_html, jpg_file,
                                css_file, js_file,
                                requests_mock):

    with open(before_html, 'r') as file:
        soup = BeautifulSoup(file, "html.parser")

    with open(jpg_file, 'rb') as file:
        jpg_mock = file.read()
    with open(css_file, 'r') as file:
        css_mock = file.read()
    with open(js_file, 'rb') as file:
        js_mock = file.read()

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


    with tempfile.TemporaryDirectory() as tmpdirname:
        path_to_file = sources_download(
            soup=soup,
            url="https://ru.hexlet.io/courses",
            temp_folder=tmpdirname
        )

        # with open(path_to_file, 'rb') as file:
        #     jpg_after_func = file.read()
        # with open(path_to_file, 'rb') as file:
        #     css_after_func = file.read()
        # with open(path_to_file, 'rb') as file:
        #     js_after_func = file.read()
        #
        # assert jpg_mock == jpg_after_func
        # assert css_mock == css_after_func
        # assert js_mock == js_after_func

        # assert jpg_mock == jpg_after_func
        # assert css_mock == css_after_func
        # assert js_mock == js_after_func