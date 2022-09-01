"""Test HTML downloader"""

import pytest
import requests
import tempfile
from bs4 import BeautifulSoup
from page_loader.download_html import html_download

# DOWNLOADER = 'download_html'


@pytest.mark.asyncio
async def test_html_download(
        before_html_path,
        result_html_path,
        requests_mock,
        urls
):
    with open(before_html_path, 'r') as file:
        soup = BeautifulSoup(file, "html.parser")

    requests_mock.get(urls['mock_url'], text=soup.prettify())
    mock_data = requests.get(urls['mock_url'], result_html_path).text

    with tempfile.TemporaryDirectory() as tmpdirname:
        _, html_file_path = html_download(soup, urls['mock_url'], tmpdirname)
        with open(html_file_path, 'r') as file:
            func_data = file.read()

        assert mock_data == func_data
