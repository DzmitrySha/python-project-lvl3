"""Test HTML downloader"""

import os
import pytest
import requests
import tempfile
from bs4 import BeautifulSoup
from page_loader.download_html import html_download

DOWNLOADER = 'download_html'


# @pytest.mark.asyncio
# async def test_html_download(before_html, result_html,
#                              result_render, requests_mock):
#
#     with open(before_html, 'r') as file:
#         soup = BeautifulSoup(file, "html.parser")
#
#     requests_mock.get("https://test.com", text=str(soup))
#     data_before = requests.get("https://test.com", before_html).text
#     data_after = requests.get("https://test.com", result_html).text
#
#     with tempfile.TemporaryDirectory() as tmpdirname:
#         path_to_file = html_download(soup, "https://test.com/", tmpdirname)
#
#         with open(path_to_file, 'r') as file:
#             data_after_func = file.read()
#
#         assert data_after == data_after_func


    # requests_mock.get('https://test.com', text='data')
    # data = requests.get('https://test.com').text
    # assert 'data' == data