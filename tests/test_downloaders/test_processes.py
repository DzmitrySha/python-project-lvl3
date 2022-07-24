"""Test processes"""

import os
import pytest
import requests
import tempfile
from bs4 import BeautifulSoup
from page_loader.processes import make_name, has_scheme, make_soup, create_dir

DOWNLOADER = 'processes'


@pytest.mark.asyncio
async def test_make_name(urls):
    http_url = urls['url']
    https_url = urls['url_s']
    assert make_name(http_url, ".html") == 'test-com.html'
    assert make_name(https_url, "_files") == 'site-test-com_files'


@pytest.mark.asyncio
async def test_has_scheme(urls):
    assert has_scheme(urls['url'])
    assert has_scheme(urls['url_s'])
    assert not has_scheme("/test.com/test")


@pytest.mark.asyncio
async def test_make_soup(before_html, urls):
    soup = make_soup(urls['mock_url'])
    assert type(soup) == BeautifulSoup


@pytest.mark.asyncio
async def test_create_dir():
    with tempfile.TemporaryDirectory() as tempdir:
        create_dir(tempdir)
        assert os.path.exists(tempdir)
        assert not os.path.exists("not_exists_dir")


@pytest.mark.asyncio
async def test_request(requests_mock):
    requests_mock.get('https://test.com', text='data')
    data = requests.get('https://test.com').text
    assert 'data' == data
