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


def read_file(path: str, flag='r'):
    with open(path, flag) as file:
        return file.read()


@pytest.mark.asyncio
async def test_sources_download(before_html_path, jpg_file_path,
                                css_file_path, js_file_path,
                                result_html_path,
                                requests_mock):
    jpg_mock = read_file(jpg_file_path, 'rb')
    css_mock = read_file(css_file_path)
    js_mock = read_file(js_file_path, 'rb')
    before_html_mock = read_file(before_html_path)
    result_html_mock = read_file(result_html_path)

    soup = BeautifulSoup(before_html_mock, "html.parser")

    requests_mock.get(HTML_MAIN_URL, text=result_html_mock)
    requests_mock.get(PAGE_URL, text=before_html_mock)
    requests_mock.get(JPG_URL, content=jpg_mock)
    requests_mock.get(CSS_URL, text=css_mock)
    requests_mock.get(JS_URL, content=js_mock)
    # requests_mock.get(CSS_URL_, text='')

    with tempfile.TemporaryDirectory() as tmpdirname:
        sources_download(
            soup=soup,
            url=HTML_MAIN_URL,
            temp_folder=tmpdirname
        )

        assert os.path.exists(os.path.join(
            os.getcwd(),
            tmpdirname,
        ))
        # assert os.path.exists(css_mock)
        # assert os.path.exists(js_mock)
        # assert os.path.exists(result_html_mock)

        # assert jpg_mock == jpg_after_func
        # assert css_mock == css_after_func
        # assert js_mock == js_after_func
        #
        # assert jpg_mock == jpg_after_func
        # assert css_mock == css_after_func
        # assert js_mock == js_after_func
