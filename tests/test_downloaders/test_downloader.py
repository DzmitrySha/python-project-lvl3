"""Test downloader"""

import os
import pytest
import tempfile
from bs4 import BeautifulSoup
from unittest.mock import Mock
from page_loader import prepare_data, downloader
from page_loader.prepare_data import make_name, make_soup, prepare_resources
from page_loader.in_out import create_dir

HTML_URL = "/courses"
PNG_URL = "/assets/professions/nodejs.png"
CSS_URL = "/assets/application.css"
JS_URL = "/script.js"
MOCK_URL = "https://cdn2.page-loader.hexlet.repl.co/blog/assets/style.css"

FILENAMES = {
    "html_mock": "page-loader-hexlet-repl-co-courses.html",
    "png_mock": "page-loader-hexlet-repl-co-assets-professions-nodejs.png",
    "css_mock": "page-loader-hexlet-repl-co-assets-application.css",
    "js_mock": "page-loader-hexlet-repl-co-script.js",
}

DIR_NAME = "page-loader-hexlet-repl-co_files"

PREPARED_RESOURCES = (
    [('/assets/application.css', 'page-loader-hexlet-repl-co_files/page-loader-hexlet-repl-co-assets-application.css'),
     ('/courses', 'page-loader-hexlet-repl-co_files/page-loader-hexlet-repl-co-courses.html'),
     ('/assets/professions/nodejs.png', 'page-loader-hexlet-repl-co_files/page-loader-hexlet-repl-co-assets-professions-nodejs.png'),
     ('/script.js', 'page-loader-hexlet-repl-co_files/page-loader-hexlet-repl-co-script.js')
     ],
    'page-loader-hexlet-repl-co.html'
)


def read_file(path: str, flag='r'):
    with open(path, flag) as file:
        return file.read()


def test_make_soup(before_html_path, urls, requests_mock):
    requests_mock.get(urls['ok_url'], text='')
    soup = make_soup(urls['ok_url'])
    assert type(soup) == BeautifulSoup


def test_make_name(urls):
    https_url = urls['ok_url']
    assert make_name(https_url, ".html") == 'page-loader-hexlet-repl-co.html'
    assert make_name(https_url, "_files") == 'page-loader-hexlet-repl-co_files'


def test_create_dir():
    with tempfile.TemporaryDirectory() as tempdir:
        create_dir(tempdir)
        assert os.path.exists(tempdir)
        assert not os.path.exists("none")


def test_make_soup_exceptions(urls):
    with pytest.raises(Exception):
        make_soup(urls['bad_url'])


def test_download(urls, file_paths,
                  before_html_path,
                  result_html_path,
                  requests_mock):
    prepare_data.prepare_resources = Mock(return_value=PREPARED_RESOURCES)
    before_html_content = read_file(before_html_path)
    html_content = read_file(file_paths[0])
    png_content = read_file(file_paths[1], 'rb')
    css_content = read_file(file_paths[2])
    js_content = read_file(file_paths[3], 'rb')
    not_exists_content = 'none'

    requests_mock.get(HTML_URL, text=html_content)
    requests_mock.get(PNG_URL, content=png_content)
    requests_mock.get(CSS_URL, text=css_content)
    requests_mock.get(JS_URL, content=js_content)
    requests_mock.get(MOCK_URL, text=not_exists_content)
    requests_mock.get(urls['ok_url'], text=before_html_content)

    with tempfile.TemporaryDirectory() as tmpdirname:
        downloader.download(urls['ok_url'], tmpdirname)
        dir_path = os.path.join(tmpdirname, DIR_NAME)

        for file_name in FILENAMES.values():
            file_path = os.path.join(tmpdirname, DIR_NAME, file_name)
            assert os.path.exists(file_path)

        with open(os.path.join(dir_path, FILENAMES["html_mock"])) as f:
            assert f.read() == html_content

        with open(os.path.join(dir_path, FILENAMES["png_mock"]), 'rb') as f:
            assert f.read() == png_content

        with open(os.path.join(dir_path, FILENAMES["css_mock"])) as f:
            assert f.read() == css_content

        with open(os.path.join(dir_path, FILENAMES["js_mock"]), 'rb') as f:
            assert f.read() == js_content

        assert not os.path.exists(os.path.join(tmpdirname, not_exists_content))


def test_prepare_resources(before_html_path, urls):

    soup = BeautifulSoup(read_file(before_html_path), "html.parser")
    prepare_data.make_soup = Mock(return_value=soup)
    prepare_data.write_to_file = Mock()

    prepared_resources = prepare_resources(urls['ok_url'])
    assert prepared_resources == PREPARED_RESOURCES


# def test_download(before_html_path, result_html_path,
#                   requests_mock, urls
#                   ):
#
#     soup = BeautifulSoup(read_file(before_html_path), "html.parser")
#     requests_mock.get(urls['ok_url'], text=soup.prettify())
#     mock_data = requests.get(urls['ok_url'], result_html_path).text
#     # print(mock_data)
#     html_file_content = read_file(result_html_path)
#
#     with tempfile.TemporaryDirectory() as tmpdirname:
#         prepare_data.prepare_resources = Mock(return_value=PREPARED_RESOURCES)
#         in_out.write_to_file = Mock()
#
#         print(html_file_content)
#         html_file_path = downloader.download(urls['ok_url'], tmpdirname)[1]
#
#         assert mock_data == html_file_content


# def test_download_resources(
#         before_html_path, jpg_file_path,
#         css_file_path, js_file_path,
#         result_html_path, html_file_path,
#         urls, requests_mock
# ):
#     before_html_content = read_file(before_html_path)
#     result_html_content = read_file(result_html_path)
#     html_content = read_file(html_file_path)
#     jpg_content = read_file(jpg_file_path, 'rb')
#     css_content = read_file(css_file_path)
#     js_content = read_file(js_file_path, 'rb')
#     mock_content = 'not_exist'
#
#     requests_mock.get(urls['ok_url'], text=result_html_content)
#     requests_mock.get(HTML_URL, text=html_content)
#     requests_mock.get(JPG_URL, content=jpg_content)
#     requests_mock.get(CSS_URL, text=css_content)
#     requests_mock.get(JS_URL, content=js_content)
#     requests_mock.get(MOCK_URL, text=mock_content)
#
#     soup = BeautifulSoup(before_html_content, "html.parser")
#
#     with tempfile.TemporaryDirectory() as tmpdirname:
#         downloader.download(urls['ok_url'], tmpdirname)
#         dir_path = os.path.join(tmpdirname, DIR_NAME)
#
#         for file_name in FILENAMES.values():
#             file_path = os.path.join(tmpdirname, DIR_NAME, file_name)
#             assert os.path.exists(file_path)
#
#         with open(os.path.join(dir_path, FILENAMES["html_mock"])) as f:
#             assert f.read() == html_content
#
#         with open(os.path.join(dir_path, FILENAMES["jpg_mock"]), 'rb') as f:
#             assert f.read() == jpg_content
#
#         with open(os.path.join(dir_path, FILENAMES["css_mock"])) as f:
#             assert f.read() == css_content
#
#         with open(os.path.join(dir_path, FILENAMES["js_mock"]), 'rb') as f:
#             assert f.read() == js_content
#
#         assert not os.path.exists(os.path.join(tmpdirname, mock_content))
