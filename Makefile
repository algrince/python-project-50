build:
	poetry build

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 gendiff
