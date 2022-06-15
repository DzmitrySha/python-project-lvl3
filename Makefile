install:
		poetry install

package-install:
		python3 -m pip install --user dist/*.whl

package-uninstall:
		python3 -m pip uninstall --yes dist/*.whl

run:
		poetry run page-loader

selfcheck:
		poetry check

test:
		poetry run pytest

test-cov:
		poetry run pytest --cov

lint:
		poetry run flake8 page_loader

test-coverage:
		poetry run pytest --cov=page_loader --cov-report xml tests/

check: selfcheck test lint

build: check
		poetry build

.PHONY: install test lint selfcheck check build