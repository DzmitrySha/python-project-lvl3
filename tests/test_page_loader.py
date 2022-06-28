"""Page loader tests"""

import os
import pytest
import requests
from unittest.mock import Mock
from page_loader.naming import make_name

FIXTURES_FOLDER = 'fixtures'


@pytest.fixture(autouse=True)
def text_html():
    """Return """
    result_path = os.path.join(os.path.dirname(__file__),
                               FIXTURES_FOLDER, 'text_html')
    with open(result_path) as file:
        return file.read()


@pytest.fixture(autouse=True)
def urls():
    urls = {
        'url': 'http://test.com',
        'url_s': 'https://site/test.com',
    }
    return urls


def test_make_name(urls):
    http_url = urls['url']
    https_url = urls['url_s']
    assert make_name(http_url, ".html") == 'test-com.html'
    assert make_name(https_url, "_files") == 'site-test-com_files'


def test_request(requests_mock):
    requests_mock.get('https://test.com', text='data')
    data = requests.get('https://test.com').text
    assert 'data' == data


# def test_download(urls):
