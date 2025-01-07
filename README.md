# Icehouse - Solana Data Lake House

Solana Data Lake House with Trino, Iceberg, DBT Core & Airflow with Cosmos.

<p align="center">
  <img src="/imgs/icehouse.jpeg" alt="icehouse">
</p>

## Overview
This project utilizes:

* **Trino (deployed on Kubernetes):** For high-performance and scalable querying
* **Apache Iceberg:** For managing data lake tables
* **dbt Core:** For data transformations
* **Airflow with Cosmos:** For orchestrating data pipelines
* **Dune Analytics:** As a data source for Solana blockchain data

## Prerequisites

- Docker & Docker Compose v2.0+
- kubectl v1.25+
- Helm v3.0+
- Python 3.9+
- Make (optional)
- Dune Analytics API key

## Project Structure

icehouse/
├── **airflow/**             _# Airflow DAGs and related files_
│   ├── **dags/**            _# Your Airflow DAGs (workflows)_
│   │   ├── **ingest_solana_data.py**  _# Airflow DAG for data ingestion_
│   │   └── **transform_data.py**      _# Airflow DAG for data transformation_
│   ├── **plugins/**         _# (Optional) Custom Airflow plugins_
│   └── **config/**          _# Airflow configuration overrides_
├── **dbt/**                 _# dbt project_
│   ├── **models/**          _# dbt models (SQL transformations)_
│   │   ├── **staging/**_
│   │   │   └── **stg_solana_transactions.sql**  _# Staging model for raw data_
│   │   ├── **intermediate/**_
│   │   │   └── **int_daily_active_accounts.sql**  _# Intermediate model with business logic_
│   │   └── **final/**_
│   │       └── **fact_account_summary.sql**      _# Final model ready for analysis_
│   ├── **macros/**                     _# Reusable SQL snippets for dbt models_
│   ├── **analyses/**                  _# Exploratory queries using dbt_
│   ├── **seeds/**                      _# Small lookup tables for dbt_
│   ├── **tests/**                      _# dbt tests for data quality checks_
│   └── **dbt_project.yml**             _# dbt project configuration_
├── **iceberg/**             _# Iceberg table schema definitions (optional)_
│   └── **schema/**                    _# Iceberg table schema definitions (optional)_
│       └── **transactions.avsc**
├── **k8s/**                            _# Kubernetes manifests_
│   ├── **trino/**_
│   │   ├── **charts/**                  _# Helm chart for deploying Trino_
│   │   │   ├── **templates/**            _# Kubernetes deployment manifests for Trino_
│   │   │   │   ├── **deployment.yaml**
│   │   │   │   └── **service.yaml**
│   │   │   └── **values.yaml**           _# Default configuration values for Trino Helm chart_
│   │   └── ...                     _# Additional Kubernetes resources for Trino (if needed)_
│   └── **metastore/**                  _# Kubernetes manifests for metastore (optional)_
│       └── **metastore-deployment.yaml**
├── **trino/**_
│   └── **queries/**                    _# Example Trino queries_
│       └── **analyze_account_activity.sql**
├── **scripts/**_
│   └── **ingest_from_blockchain.py**    _# Script for data ingestion from blockchain_
├── **data/**_
│   └── **sample_transactions.json**     _# Sample data for testing (small dataset)_
├── **tests/**_
│   └── **test_ingestion.py**           _# Unit test for data ingestion script_
├── **Dockerfile**                      _# Dockerfile for containerization (optional)_
├── **docker-compose.yml**             _# Docker Compose for local development (simplified)_
├── **requirements.txt**                _# Python dependencies_
└── **README.md**                       _# Project documentation_


## Quick Start

1. Clone the repository: `git clone git@github.com:karolsudol/icehouse.git`
2. Create a virtual environment: `python -m venv .venv`
3. Activate the virtual environment: `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

## Key Components

* `airflow/`: Contains all Airflow-related configurations and DAGs for data ingestion and transformation.
* `dbt/`: Houses the dbt Core project for data transformations, defining models for raw, intermediate, and final data states.
* `k8s/`: This new directory holds Kubernetes manifests for deploying Trino and potentially other services (like a metastore). The `trino/` subdirectory contains a Helm chart for deploying Trino using Kubernetes best practices.
* `iceberg/` (optional): If you're managing Iceberg







### Key Components:
- `airflow/`: Contains all Airflow-related configurations and DAGs
- `dbt/`: Houses the dbt Core project for data transformations
- `k8s/`: Kubernetes manifests for Trino and other services
- `scripts/`: Utility scripts for setup and maintenance






### Modifying Airflow DAGs
1. Edit or add DAGs in `airflow/dags/`
2. DAGs will be automatically picked up by Airflow

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## Data Flow
1. Airflow DAG fetches daily Solana transaction data from Dune Analytics
2. Data is stored in Iceberg tables in MinIO
3. dbt models transform the raw data
4. Results can be queried via Trino

## Development

### Adding New dbt Models
1. Create new models in `dbt/models/solana/`
2. Update `schema.yml` and `sources.yml`
3. Test locally:





