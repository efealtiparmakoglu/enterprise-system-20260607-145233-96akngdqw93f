.PHONY: install test lint format clean build run docker

install:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

test:
	pytest tests/ -v --cov=src

lint:
	flake8 src/ --count --select=E9,F63,F7,F82 --show-source --statistics
	black src/ --check

format:
	black src/
	isort src/

clean:
	rm -rf __pycache__/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build:
	docker build -t $(repo_name):latest .

run:
	uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

docker:
	docker-compose up -d

migrate:
	alembic revision --autogenerate -m "Auto migration"
	alembic upgrade head
