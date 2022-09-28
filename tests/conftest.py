"""fixtures"""

import os
import pytest

FIXTURES_FOLDER = 'fixtures'
EXPECTED_FOLDER = 'fixtures/expected'
EXPECTED_FILES_FOLDER = 'fixtures/expected/page-loader-hexlet-repl-co_files'
FILES_PATHS = ['page-loader-hexlet-repl-co-courses.html',
               'page-loader-hexlet-repl-co-assets-professions-nodejs.png',
               'page-loader-hexlet-repl-co-assets-application.css',
               'page-loader-hexlet-repl-co-script.js'
               ]


@pytest.fixture
def file_paths():
    file_paths = [
        os.path.join(os.path.dirname(__file__), EXPECTED_FILES_FOLDER, path)
        for path in FILES_PATHS
    ]
    return file_paths


@pytest.fixture
def before_html_path():
    return os.path.join(os.path.dirname(__file__), FIXTURES_FOLDER,
                        'page-loader-hexlet-repl-co.html'
                        )


@pytest.fixture
def result_html_path():
    return os.path.join(os.path.dirname(__file__), EXPECTED_FOLDER,
                        'page-loader-hexlet-repl-co.html'
                        )


@pytest.fixture
def urls():
    urls = {
        'ok_url': "https://page-loader.hexlet.repl.co",
        'bad_url': 'site.com',
    }
    return urls
