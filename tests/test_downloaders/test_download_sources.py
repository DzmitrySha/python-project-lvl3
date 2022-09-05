"""Test sources downloader"""

import os
import pytest
import tempfile
from bs4 import BeautifulSoup
from page_loader.download_sources import sources_download, prepare_sources_urls


HTML_URL = "/courses"
JPG_URL = "/assets/professions/nodejs.png"
CSS_URL = "/assets/application.css"
JS_URL = "/script.js"
MOCK_URL = "https://cdn2.page-loader.hexlet.repl.co/blog/assets/style.css"
SOURCES_URLS = ['/assets/application.css', '/courses',
                '/assets/professions/nodejs.png', '/script.js']


DIR_NAME = "page-loader-hexlet-repl-co_files"
FILENAMES = {
    "html_mock": "page-loader-hexlet-repl-co-courses.html",
    "jpg_mock": "page-loader-hexlet-repl-co-assets-professions-nodejs.png",
    "css_mock": "page-loader-hexlet-repl-co-assets-application.css",
    "js_mock": "page-loader-hexlet-repl-co-script.js",
}


def read_file(path: str, flag='r'):
    with open(path, flag) as file:
        return file.read()


@pytest.mark.asyncio
async def test_prepare_sources_urls(before_html_path, urls):
    soup = BeautifulSoup(read_file(before_html_path), 'html.parser')
    sources_list = prepare_sources_urls(soup, urls['https_url'])
    assert sources_list == SOURCES_URLS


@pytest.mark.asyncio
async def test_sources_download(
        before_html_path, jpg_file_path,
        css_file_path, js_file_path,
        result_html_path, html_file_path,
        urls, requests_mock
):
    before_html_content = read_file(before_html_path)
    result_html_content = read_file(result_html_path)
    html_content = read_file(html_file_path)
    jpg_content = read_file(jpg_file_path, 'rb')
    css_content = read_file(css_file_path)
    js_content = read_file(js_file_path, 'rb')
    mock_content = 'not_exist'

    requests_mock.get(urls['https_url'], text=result_html_content)
    requests_mock.get(HTML_URL, text=html_content)
    requests_mock.get(JPG_URL, content=jpg_content)
    requests_mock.get(CSS_URL, text=css_content)
    requests_mock.get(JS_URL, content=js_content)
    requests_mock.get(MOCK_URL, text=mock_content)

    soup = BeautifulSoup(before_html_content, "html.parser")

    with tempfile.TemporaryDirectory() as tmpdirname:
        sources_download(soup, urls['https_url'], tmpdirname)
        dir_path = os.path.join(tmpdirname, DIR_NAME)

        for file_name in FILENAMES.values():
            file_path = os.path.join(tmpdirname, DIR_NAME, file_name)
            assert os.path.exists(file_path)

        with open(os.path.join(dir_path, FILENAMES["html_mock"])) as f:
            assert f.read() == html_content

        with open(os.path.join(dir_path, FILENAMES["jpg_mock"]), 'rb') as f:
            assert f.read() == jpg_content

        with open(os.path.join(dir_path, FILENAMES["css_mock"])) as f:
            assert f.read() == css_content

        with open(os.path.join(dir_path, FILENAMES["js_mock"]), 'rb') as f:
            assert f.read() == js_content

        assert not os.path.exists(os.path.join(tmpdirname, mock_content))
