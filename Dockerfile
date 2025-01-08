# Use Python base image
FROM python:3.9-slim

WORKDIR /app

# Create and activate virtual environment, install trino provider
RUN python -m venv /app/dbt_venv && \
    . /app/dbt_venv/bin/activate && \
    pip install --no-cache-dir apache-airflow-providers-trino && \
    pip install dbt-trino

# Add virtual environment to PATH using absolute path
ENV PATH="/app/dbt_venv/bin:$PATH"