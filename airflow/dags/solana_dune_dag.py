from cosmos import DbtDag, ProjectConfig, ProfileConfig
from datetime import datetime

profile_config = ProfileConfig(
    profile_name="icehouse",
    target_name="dev",
    profiles_yml_filepath="/opt/airflow/dags/cosmos_config/profiles.yml"
)

project_config = ProjectConfig(
    dbt_project_path="/opt/airflow/dags/dbt",
)

solana_dag = DbtDag(
    dag_id="solana_daily_sync",
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 1),
    project_config=project_config,
    profile_config=profile_config,
    default_args={"owner": "airflow"},
) 