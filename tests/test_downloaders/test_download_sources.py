"""Test sources downloader"""

import os
import pytest
import tempfile
import requests
from bs4 import BeautifulSoup
from page_loader.download_sources import sources_download


# HTML_MAIN_URL = "https://ru.hexlet.io"
# PAGE_URL = "https://ru.hexlet.io/courses"
# JPG_URL = "https://ru.hexlet.io/assets/professions/python.jpg"
# CSS_URL = "https://ru.hexlet.io/assets/application.css"
# JS_URL = "https://ru.hexlet.io/packs/js/runtime.js"
# MOCK_URL = "https://cdn2.hexlet.io/assets/menu.css"
#
# DIR_NAME = "ru-hexlet-io_files"
# FILENAMES = {
#     "page_url_name": "ru-hexlet-io-courses",
#     "jpg_mock": "ru-hexlet-io-assets-professions-python.jpg",
#     "css_mock": "ru-hexlet-io-assets-application.css",
#     "js_mock": "ru-hexlet-io-packs-js-runtime.js",
# }


HTML_MAIN_URL = "https://site.com"
PAGE_URL = "https://site.com/blog/about"
JPG_URL = "https://site.com/photos/me.jpg"
CSS_URL = "https://site.com/blog/about/assets/styles.css"
JS_URL = "https://site.com/assets/scripts.js"
MOCK_URL = "https://cdn2.site.com/blog/assets/style.css"


DIR_NAME = "site-com_files"
FILENAMES = {
    "page_url_name": "site-com-blog-about",
    "jpg_mock": "site-com-photos-me.jpg",
    "css_mock": "site-com-blog-about-assets-styles.css",
    "js_mock": "site-com-assets-scripts.js",
}


def read_file(path: str, flag='r'):
    with open(path, flag) as file:
        return file.read()


@pytest.mark.asyncio
async def test_sources_download(
        before_html_path, jpg_file_path,
        css_file_path, js_file_path,
        result_html_path, urls,
        requests_mock
):
    before_html_content = read_file(before_html_path)
    result_html_content = read_file(result_html_path)
    jpg_content = read_file(jpg_file_path, 'rb')
    css_content = read_file(css_file_path)
    js_content = read_file(js_file_path, 'rb')
    mock_content = 'not_exist'

    requests_mock.get(HTML_MAIN_URL, text=result_html_content)
    # assert result_html_content == requests.get(HTML_MAIN_URL).text

    requests_mock.get(PAGE_URL, text=before_html_content)
    # assert before_html_content == requests.get(PAGE_URL).text

    requests_mock.get(JPG_URL, content=jpg_content)
    # assert jpg_content == requests.get(JPG_URL).content

    requests_mock.get(CSS_URL, text=css_content)
    # assert css_content == requests.get(CSS_URL).text

    requests_mock.get(JS_URL, content=js_content)
    # assert js_content == requests.get(JS_URL).content

    requests_mock.get(MOCK_URL, text=mock_content)
    # assert mock_content == requests.get(MOCK_URL).text

    soup = BeautifulSoup(before_html_content, "html.parser")

    with tempfile.TemporaryDirectory() as tmpdirname:
        sources_download(soup, HTML_MAIN_URL, tmpdirname)
        for file_name in FILENAMES.values():
            file_path = os.path.join(DIR_NAME, file_name)
            assert os.path.exists(os.path.join(tmpdirname, file_path))
        assert not os.path.exists(os.path.join(tmpdirname, mock_content))
