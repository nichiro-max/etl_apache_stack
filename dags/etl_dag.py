from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import subprocess

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2024, 8, 5),
}

dag = DAG(
    'spark_etl_dag',
    default_args=default_args,
    description='An ETL DAG using Spark, Kafka, and Delta Lake',
    schedule_interval='@daily',
)

def run_spark_job():
    subprocess.run(["spark-submit", "--master", "spark://spark:7077", "/app/spark_etl.py"])

run_spark = PythonOperator(
    task_id='run_spark_etl',
    python_callable=run_spark_job,
    dag=dag,
)

run_spark
