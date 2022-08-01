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
def before_html():
    return os.path.join(os.path.dirname(__file__),
                        FIXTURES_FOLDER, 'before.html')


@pytest.fixture(scope="session")
def result_html():
    return os.path.join(os.path.dirname(__file__),
                        FIXTURES_FOLDER, 'result.html')


@pytest.fixture(scope="session")
def jpg_file():
    return os.path.join(os.path.dirname(__file__),
                        FIXTURES_FOLDER, 'python.jpg')


@pytest.fixture(scope="session")
def css_file():
    return os.path.join(os.path.dirname(__file__),
                        FIXTURES_FOLDER, 'style.css')


@pytest.fixture(scope="session")
def js_file():
    return os.path.join(os.path.dirname(__file__),
                        FIXTURES_FOLDER, 'script.js')


@pytest.fixture(scope="session")
def urls():
    mock = Mock()
    mock.url = "https://ru.hexlet.io"
    urls = {
        'url': 'http://test.com',
        'url_s': 'https://site/test.com',
        'mock_url': mock.url,
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
