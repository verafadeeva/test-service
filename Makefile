all: poetry

initial: 
	python3 db/initial_db.py

poetry: poetry-inst
	poetry shell

poetry-inst:
	poetry install --no-root