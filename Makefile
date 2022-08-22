install:
	poetry install

build:
	poetry build

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff

check:
	selfcheck test lint

selfcheck:
	poetry check
