"""Test processes"""

import os
import pytest
import requests
import tempfile
from bs4 import BeautifulSoup
from page_loader.processes import make_name, make_soup, create_dir


@pytest.mark.asyncio
async def test_make_soup(before_html_path, urls, requests_mock):
    requests_mock.get(urls['http_url'], text='data')
    data = requests.get(urls['http_url']).text
    soup = make_soup(urls['http_url'])
    assert type(soup) == BeautifulSoup


@pytest.mark.asyncio
async def test_make_name(urls):
    http_url = urls['http_url']
    https_url = urls['https_url']
    assert make_name(http_url, ".html") == 'site-com.html'
    assert make_name(http_url, "_files") == 'site-com_files'
    assert make_name(https_url, ".html") == 'site-com-test.html'
    assert make_name(https_url, "_files") == 'site-com-test_files'


@pytest.mark.asyncio
async def test_create_dir():
    with tempfile.TemporaryDirectory() as tempdir:
        create_dir(tempdir)
        assert os.path.exists(tempdir)
        assert not os.path.exists("none")


@pytest.mark.asyncio
async def test_make_soup_exc(urls):
    with pytest.raises(Exception):
        make_soup(urls['bad_url'])
