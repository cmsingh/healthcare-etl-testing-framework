from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from tests.test_etl_validations import test_end_to_end_etl

with DAG(
    dag_id="healthcare_etl_validation",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    validate_etl = PythonOperator(
        task_id="validate_healthcare_etl",
        python_callable=test_end_to_end_etl
    )

    validate_etl


with DAG(
    dag_id="healthcare_etl_validation_prod",
    schedule_interval="@hourly",
    catchup=False
) as dag:

    extract = PythonOperator(...)
    transform = PythonOperator(...)
    load = PythonOperator(...)

    validate_bq = PythonOperator(
        task_id="validate_bigquery_data",
        python_callable=run_bigquery_validations
    )

    extract >> transform >> load >> validate_bq
