"""Test sources downloader"""

import os
import pytest
import tempfile
from bs4 import BeautifulSoup
from page_loader.download_sources import sources_download, prepare_sources_urls


PAGE_URL = "/courses"
JPG_URL = "/assets/professions/nodejs.png"
CSS_URL = "/assets/application.css"
JS_URL = "/script.js"
MOCK_URL = "https://cdn2.site.com/blog/assets/style.css"
SOURCES_URLS = ['/assets/application.css', '/courses',
                '/assets/professions/nodejs.png', '/script.js']


DIR_NAME = "page-loader-hexlet-repl-co_files"
FILENAMES = {
    "page_url_name": "page-loader-hexlet-repl-co-courses",
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
        result_html_path, urls,
        requests_mock
):
    before_html_content = read_file(before_html_path)
    result_html_content = read_file(result_html_path)
    jpg_content = read_file(jpg_file_path, 'rb')
    css_content = read_file(css_file_path)
    js_content = read_file(js_file_path, 'rb')
    mock_content = 'not_exist'

    requests_mock.get(urls['https_url'], text=result_html_content)
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
        sources_download(soup, urls['https_url'], tmpdirname)
        for file_name in FILENAMES.values():
            file_path = os.path.join(DIR_NAME, file_name)
            assert os.path.exists(os.path.join(tmpdirname, file_path))
        assert not os.path.exists(os.path.join(tmpdirname, mock_content))
