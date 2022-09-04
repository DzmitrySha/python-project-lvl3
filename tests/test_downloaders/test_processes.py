"""Test processes"""

import os
import pytest
import tempfile
from bs4 import BeautifulSoup
from page_loader.processes import make_name, make_soup, create_dir


@pytest.mark.asyncio
async def test_make_soup(before_html_path, urls, requests_mock):
    requests_mock.get(urls['https_url'], text='')
    soup = make_soup(urls['https_url'])
    assert type(soup) == BeautifulSoup


@pytest.mark.asyncio
async def test_make_name(urls):
    https_url = urls['https_url']
    assert make_name(https_url, ".html") == 'page-loader-hexlet-repl-co.html'
    assert make_name(https_url, "_files") == 'page-loader-hexlet-repl-co_files'


@pytest.mark.asyncio
async def test_create_dir():
    with tempfile.TemporaryDirectory() as tempdir:
        create_dir(tempdir)
        assert os.path.exists(tempdir)
        assert not os.path.exists("none")


@pytest.mark.asyncio
async def test_make_soup_exceptions(urls):
    with pytest.raises(Exception):
        make_soup(urls['bad_url'])
