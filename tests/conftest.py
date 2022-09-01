"""fixtures"""

import os
import asyncio
import pytest
from unittest.mock import Mock

FIXTURES_FOLDER = 'fixtures'


@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def before_html_path():
    return os.path.join(os.path.dirname(__file__),
                        FIXTURES_FOLDER, 'before.html')


@pytest.fixture(scope="session")
def result_html_path():
    return os.path.join(os.path.dirname(__file__),
                        FIXTURES_FOLDER, 'result.html')


@pytest.fixture(scope="session")
def jpg_file_path():
    return os.path.join(os.path.dirname(__file__),
                        FIXTURES_FOLDER, 'python.jpg')


@pytest.fixture(scope="session")
def css_file_path():
    return os.path.join(os.path.dirname(__file__),
                        FIXTURES_FOLDER, 'style.css')


@pytest.fixture(scope="session")
def js_file_path():
    return os.path.join(os.path.dirname(__file__),
                        FIXTURES_FOLDER, 'script.js')


@pytest.fixture(scope="session")
def urls():
    mock = Mock()
    mock.url = "https://site.io"
    mock.url_exc = "site.io"
    urls = {
        'http_url': 'http://test.com',
        'https_url': 'https://site/test.com',
        'mock_url': mock.url,
        'mock_url_exc': mock.url_exc,
    }
    return urls


# @pytest.fixture(scope="function")
# async def result_render(request):
#     assert getattr(request.module, 'DOWNLOADER', None)
#
#     result_path = os.path.join(os.path.dirname(__file__),
#                                FIXTURES_FOLDER, request.module.DOWNLOADER)
#
#     with open(result_path) as file:
#         return file.read()
