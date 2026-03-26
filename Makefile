# OpenVault Project Automation Makefile
.PHONY: help install run test lint db-init seed backup clean docker-build docker-up

help:
	@echo "OpenVault Development Commands:"
	@echo "  make install      - Install python dependencies"
	@echo "  make run          - Run local development server"
	@echo "  make test         - Run full pytest test suite"
	@echo "  make db-init      - Initialize sqlite database schema"
	@echo "  make seed         - Seed database with demo data"
	@echo "  make backup       - Run database backup script"
	@echo "  make clean        - Remove caches and test artifacts"
	@echo "  make docker-build - Build Docker image"
	@echo "  make docker-up    - Start container via docker-compose"

install:
	pip install -r requirements.txt

run:
	python -m app.main --debug

test:
	pytest

db-init:
	python scripts/setup.py

seed:
	python scripts/seed_database.py

backup:
	python scripts/backup.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .coverage htmlcov test_*.db

docker-build:
	docker build -t openvault:latest .

docker-up:
	docker compose up -d
