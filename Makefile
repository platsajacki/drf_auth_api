lint:
	python3 auth_api/manage.py check
	flake8 .
	mypy .

test:
	pytest --cov=.
