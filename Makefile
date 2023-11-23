all: initial-db

initial-db: poetry
	python db/initial_db.py

poetry: poetry-inst
	poetry shell

poetry-inst:
	poetry install --no-root