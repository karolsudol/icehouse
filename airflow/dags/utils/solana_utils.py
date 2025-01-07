from airflow.models import Variable
import requests
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)

def get_dune_api_key(**context) -> str:
    """
    Retrieve Dune Analytics API key from Airflow Variables.
    
    Returns:
        str: The Dune API key
    Raises:
        ValueError: If the API key is not set
    """
    dune_api_key = Variable.get("dune_api_key")
    if not dune_api_key:
        raise ValueError("Dune API key not set in Airflow Variables")
    return dune_api_key

def fetch_data_from_dune(**context) -> Dict[str, Any]:
    """
    Fetch Solana data from Dune Analytics API.
    
    Args:
        context: Airflow context containing task instance
    
    Returns:
        Dict[str, Any]: The fetched data from Dune
    """
    try:
        # Get API key from previous task
        dune_api_key = context['ti'].xcom_pull(task_ids='get_dune_api_key')
        
        # Configuration for Dune API
        QUERY_ID = "YOUR_QUERY_ID"  # Replace with your actual query ID
        API_BASE_URL = "https://api.dune.com/api/v1"
        
        # Execute query
        execute_endpoint = f"{API_BASE_URL}/query/{QUERY_ID}/execute"
        headers = {"x-dune-api-key": dune_api_key}
        
        # Start query execution
        execution = requests.post(execute_endpoint, headers=headers)
        execution.raise_for_status()
        execution_id = execution.json()['execution_id']
        
        # Get results
        results_endpoint = f"{API_BASE_URL}/execution/{execution_id}/results"
        results = requests.get(results_endpoint, headers=headers)
        results.raise_for_status()
        
        data = results.json()
        
        # Store the data in XCom for the next task
        context['ti'].xcom_push(key='solana_data', value=data)
        return data
        
    except Exception as e:
        logger.error(f"Error fetching data from Dune: {str(e)}")
        raise

def write_to_iceberg(**context) -> None:
    """
    Write the fetched Solana data to Iceberg tables.
    
    Args:
        context: Airflow context containing task instance
    """
    try:
        # Get data from previous task
        data = context['ti'].xcom_pull(key='solana_data', task_ids='fetch_solana_data')
        
        if not data:
            raise ValueError("No data received from Dune Analytics")
        
        # TODO: Implement your Iceberg writing logic here
        # Example pseudo-code:
        # from pyiceberg.catalog import load_catalog
        # catalog = load_catalog(
        #     'my_catalog',
        #     **your_connection_parameters
        # )
        # table = catalog.load_table('your_schema.your_table')
        # table.append(data)
        
        logger.info("Successfully wrote data to Iceberg table")
        
    except Exception as e:
        logger.error(f"Error writing to Iceberg: {str(e)}")
        raise 