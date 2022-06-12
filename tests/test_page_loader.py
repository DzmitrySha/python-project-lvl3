# Page loader tests

import os
import pytest
# import requests
# import requests_mock
from unittest.mock import Mock
from page_loader.page_loader import download

FIXTURES_FOLDER = 'fixtures'


@pytest.fixture
def text_html():
    result_path = os.path.join(os.path.dirname(__file__),
                               FIXTURES_FOLDER, 'page_text')
    with open(result_path) as file:
        return file.read()


# @pytest.fixture
# def test_simple(requests_mock):
#     requests_mock.get('https://ru.hexlet.io/courses/prog-life', text='data')
#     assert 'data' ==
#     requests.get('https://ru.hexlet.io/courses/prog-life').text
#
#
def test_save_file(text_html):
    mock = Mock()
    mock.result = 'some pretty html code'
    assert mock.result == text_html
