from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from utils.solana_utils import get_dune_api_key, fetch_data_from_dune, write_to_iceberg

# Define default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'execution_timeout': timedelta(hours=1),
}

# Define DAG
dag = DAG(
    dag_id='ingest_solana_data',
    default_args=default_args,
    description='Ingest Solana data from Dune Analytics to Iceberg',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),  # Explicit start date instead of days_ago
    catchup=False,
    tags=['solana', 'ingestion', 'dune', 'iceberg'],
)

# Define tasks
get_dune_api_key_task = PythonOperator(
    task_id='get_dune_api_key',  # Simplified task name
    python_callable=get_dune_api_key,
    dag=dag,
)

fetch_data_task = PythonOperator(
    task_id='fetch_solana_data',
    python_callable=fetch_data_from_dune,
    dag=dag,
)

write_to_iceberg_task = PythonOperator(
    task_id='write_to_iceberg',
    python_callable=write_to_iceberg,
    dag=dag,
)

# Set dependencies
get_dune_api_key_task >> fetch_data_task >> write_to_iceberg_task