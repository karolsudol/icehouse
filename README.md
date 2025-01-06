# Icehouse - Solana Data Lake House

Solana Data Lake House with Trino, Iceberg, DBT Core & Airflow with Cosmos.

<p align="center">
  <img src="/imgs/icehouse.jpeg" alt="icehouse">
</p>

## Overview
This project sets up a complete data lakehouse solution for Solana blockchain data using:
- Trino for querying
- Apache Iceberg for data lake management
- dbt Core for transformations
- Airflow with Cosmos for orchestration
- Dune Analytics as data source

## Prerequisites
- Docker & Docker Compose v2.0+
- kubectl v1.25+
- Helm v3.0+
- Python 3.9+
- Make (optional)
- Dune Analytics API key

## Project Structure

## Project Structure


icehouse/


## Quick Start

1. Clone the repository: 
2. python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

# This will install apache-airflow-providers-cosmos and its dependencies.

# To deactivate the virtual environment when you're done:
deactivate






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





