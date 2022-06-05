# Page loader tests

import os
import pytest
from page_loader.page_loader import download
from unittest.mock import Mock

FIXTURES_FOLDER = 'fixtures'


@pytest.fixture
def text_html():
    result_path = os.path.join(os.path.dirname(__file__),
                               FIXTURES_FOLDER, 'page_text')
    with open(result_path) as file:
        return file.read()


def test_download(text_html):
    pass
    # mock = Mock()
    # mock.page = 'https://'
    # assert download(mock.page) == ''
