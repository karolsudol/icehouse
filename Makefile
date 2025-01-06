.PHONY: setup start stop clean help k8s-setup dbt-run

# Colors for terminal output
GREEN  := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
WHITE  := $(shell tput -Txterm setaf 7)
RESET  := $(shell tput -Txterm sgr0)

help: ## Show this help
	@echo ''
	@echo 'Usage:'
	@echo '  ${YELLOW}make${RESET} ${GREEN}<target>${RESET}'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  ${YELLOW}%-15s${GREEN}%s${RESET}\n", $$1, $$2}' $(MAKEFILE_LIST)

setup: ## Initial setup of the project
	@echo "Setting up the project..."
	cp -n .env.example .env || true
	docker-compose build
	./scripts/setup.sh
	@echo "Setup complete! Run 'make start' to start the services"

start: ## Start all services
	docker-compose up -d
	@echo "Services are starting..."
	@echo "Airflow: http://localhost:8080"
	@echo "MinIO Console: http://localhost:9001"
	@echo "Trino: http://localhost:8081"

stop: ## Stop all services
	docker-compose down
	@echo "Services stopped"

clean: ## Clean up all containers and volumes
	docker-compose down -v
	rm -rf airflow/logs/*
	rm -rf airflow/plugins/*
	rm -rf dbt/target
	rm -rf dbt/dbt_packages
	@echo "Clean up complete"

k8s-setup: ## Setup Kubernetes components (Trino & MinIO)
	@echo "Setting up Kubernetes components..."
	helm repo add trino https://trinodb.github.io/charts
	helm repo add minio https://charts.min.io/
	helm repo update
	kubectl create namespace icehouse || true
	helm upgrade --install minio minio/minio -f k8s/minio/values.yaml -n icehouse
	helm upgrade --install trino trino/trino -f k8s/trino/values.yaml -n icehouse
	@echo "Kubernetes setup complete"

dbt-run: ## Run dbt models
	@echo "Running dbt models..."
	cd dbt && dbt deps && dbt run

logs: ## View logs of all services
	docker-compose logs -f

test: ## Run tests
	cd dbt && dbt test
	# Add more test commands here

init-dev: setup start ## Initialize development environment
	@echo "Development environment ready!" 