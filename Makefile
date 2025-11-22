.DEFAULT_GOAL := run

TYPE ?= local

run: ## RUN WEB-SEVER AND PYTHON SCRIPT
	uv run uvicorn --reload main:app --env-file .$(TYPE).env

help:
	@echo '================================================'
	@echo 'HELP DOESNT COME'
	@echo 'GO TO PLAKAT POD MOSTOM'
	@echo '================================================'


migrate:
	uv run alembic revision --autogenerate -m ${MESSAGE}

mupdate:
	uv run alembic upgrade head
	
docker:
	docker-compose up -d