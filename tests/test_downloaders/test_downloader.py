"""Test downloader"""

# import pytest
# import requests
# import tempfile
# from bs4 import BeautifulSoup
# from page_loader.downloader import download
#

# @pytest.mark.asyncio
# async def test_download(
#         before_html_path,
#         result_html_path,
#         requests_mock,
#         urls
# ):
#     with open(before_html_path, 'r') as file:
#         soup = BeautifulSoup(file, "html.parser")
#
#     requests_mock.get(urls['https_url'], text=soup.prettify())
#     mock_data = requests.get(urls['https_url'], result_html_path).text
#
#     with tempfile.TemporaryDirectory() as tmpdirname:
#         html_file_path = download(urls['https_url'], tmpdirname)
#         with open(html_file_path, 'r') as file:
#             html_file_content = file.read()
#
#         assert mock_data == html_file_content
