"""Test processes"""

import os
import pytest
import requests
import tempfile
from bs4 import BeautifulSoup
from page_loader.processes import (make_name, make_soup,
                                   create_dir, is_folder_exists)

# DOWNLOADER = 'processes'


@pytest.mark.asyncio
async def test_is_folder_exists():
    folder_path = os.getcwd()
    assert is_folder_exists(folder_path) is True


@pytest.mark.asyncio
async def test_make_soup(before_html, urls):
    soup = make_soup(urls['mock_url'])
    assert type(soup) == BeautifulSoup


@pytest.mark.asyncio
async def test_make_name(urls):
    http_url = urls['url']
    https_url = urls['url_s']
    assert make_name(http_url, ".html") == 'test-com.html'
    assert make_name(https_url, "_files") == 'site-test-com_files'


@pytest.mark.asyncio
async def test_create_dir():
    with tempfile.TemporaryDirectory() as tempdir:
        create_dir(tempdir)
        assert os.path.exists(tempdir)
        assert not os.path.exists("not_exists_dir")


@pytest.mark.asyncio
async def test_request(urls, requests_mock):
    requests_mock.get(urls['url'], text='data')
    data = requests.get(urls['url']).text
    assert 'data' == data
