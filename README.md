
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

```
icehouse/
├── airflow/             # Airflow DAGs and related files
│   ├── dags/            # Your Airflow DAGs (workflows)
│   │   ├── ingest_solana_data.py  # Airflow DAG for data ingestion
│   │   └── transform_data.py      # Airflow DAG for data transformation
│   ├── plugins/         # (Optional) Custom Airflow plugins
│   └── config/          # Airflow configuration overrides
├── dbt/                 # dbt project
│   ├── models/          # dbt models (SQL transformations)
│   │   ├── staging/
│   │   │   └── stg_solana_transactions.sql  # Staging model for raw data
│   │   ├── intermediate/
│   │   │   └── int_daily_active_accounts.sql  # Intermediate model with business logic
│   │   └── final/
│   │       └── fact_account_summary.sql      # Final model ready for analysis
│   ├── macros/                     # Reusable SQL snippets for dbt models
│   ├── analyses/                  # Exploratory queries using dbt
│   ├── seeds/                      # Small lookup tables for dbt
│   ├── tests/                      # dbt tests for data quality checks
│   └── dbt_project.yml             # dbt project configuration
├── iceberg/             # Iceberg table schema definitions (optional)
│   └── schema/                    # Iceberg table schema definitions (optional)
│       └── transactions.avsc
├── k8s/                            # Kubernetes manifests
│   ├── trino/
│   │   ├── charts/                  # Helm chart for deploying Trino
│   │   │   ├── templates/            # Kubernetes deployment manifests for Trino
│   │   │   │   ├── deployment.yaml
│   │   │   │   └── service.yaml
│   │   │   └── values.yaml           # Default configuration values for Trino Helm chart
│   │   └── ...                     # Additional Kubernetes resources for Trino (if needed)
│   └── metastore/                  # Kubernetes manifests for metastore (optional)
│       └── metastore-deployment.yaml
├── trino/
│   └── queries/                    # Example Trino queries
│       └── analyze_account_activity.sql
├── scripts/
│   └── ingest_from_blockchain.py    # Script for data ingestion from blockchain
├── data/
│   └── sample_transactions.json     # Sample data for testing (small dataset)
├── tests/
│   └── test_ingestion.py           # Unit test for data ingestion script
├── Dockerfile                      # Dockerfile for containerization (optional)
├── docker-compose.yml             # Docker Compose for local development (simplified)
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

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
