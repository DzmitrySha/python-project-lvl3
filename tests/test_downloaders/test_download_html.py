"""Test HTML downloader"""

import pytest
import requests
import tempfile
from bs4 import BeautifulSoup
from page_loader.download_html import html_download

DOWNLOADER = 'download_html'


@pytest.mark.asyncio
async def test_html_download(before_html, result_html, requests_mock):

    with open(before_html, 'r') as file:
        soup = BeautifulSoup(file, "html.parser")

    requests_mock.get("https://ru.hexlet.io", text=soup.prettify())
    data_after_mock = requests.get("https://ru.hexlet.io", result_html).text

    with tempfile.TemporaryDirectory() as tmpdirname:
        path_to_file = html_download(soup, "https://ru.hexlet.io", tmpdirname)
        with open(path_to_file, 'r') as file:
            data_after_func = file.read()

        assert data_after_mock == data_after_func
