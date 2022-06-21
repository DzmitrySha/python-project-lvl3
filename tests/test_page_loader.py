"""Page loader tests"""

import os
import pytest
import requests
from unittest.mock import Mock
from page_loader.page_loader import download, url_to_filename

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


def test_url_to_filename(urls):
    http_url = urls['url']
    https_url = urls['url_s']
    assert url_to_filename(http_url) == 'test-com.html'
    assert url_to_filename(https_url) == 'site-test-com.html'


def test_request(requests_mock):
    requests_mock.get('https://test.com', text='data')
    data = requests.get('https://test.com').text
    assert 'data' == data


# def test_download(urls):
