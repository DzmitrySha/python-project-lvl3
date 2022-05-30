install:
		poetry install

package-install:
		python3 -m pip install --user dist/*.whl

package-uninstall:
		python3 -m pip uninstall --yes dist/*.whl

selfcheck:
		poetry check

test:
		poetry run pytest

lint:
		poetry run flake8 page_loader

test-coverage:
		poetry run pytest --cov=page_loader --cov-report xml tests/

check: selfcheck test lint

build: check
		poetry build

.PHONY: install test lint selfcheck check build