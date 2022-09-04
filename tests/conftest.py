"""fixtures"""

import os
import asyncio
import pytest

FIXTURES_FOLDER = 'fixtures'
EXPECTED_FOLDER = 'fixtures/expected'
EXPECTED_FILES_FOLDER = 'fixtures/expected/page-loader-hexlet-repl-co_files'


@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def before_html_path():
    return os.path.join(os.path.dirname(__file__), FIXTURES_FOLDER,
                        'page-loader-hexlet-repl-co.html'
                        )


@pytest.fixture(scope="session")
def result_html_path():
    return os.path.join(os.path.dirname(__file__), EXPECTED_FOLDER,
                        'page-loader-hexlet-repl-co.html'
                        )


@pytest.fixture(scope="session")
def html_file_path():
    return os.path.join(
        os.path.dirname(__file__), EXPECTED_FILES_FOLDER,
        'page-loader-hexlet-repl-co-courses.html'
    )



@pytest.fixture(scope="session")
def jpg_file_path():
    return os.path.join(
        os.path.dirname(__file__), EXPECTED_FILES_FOLDER,
        'page-loader-hexlet-repl-co-assets-professions-python.jpg'
    )


@pytest.fixture(scope="session")
def css_file_path():
    return os.path.join(os.path.dirname(__file__), EXPECTED_FILES_FOLDER,
                        'page-loader-hexlet-repl-co-assets-application.css'
                        )


@pytest.fixture(scope="session")
def js_file_path():
    return os.path.join(os.path.dirname(__file__), EXPECTED_FILES_FOLDER,
                        'page-loader-hexlet-repl-co-script.js'
                        )


@pytest.fixture(scope="session")
def urls():
    urls = {
        'https_url': "https://page-loader.hexlet.repl.co",
        'bad_url': 'site.com',
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
