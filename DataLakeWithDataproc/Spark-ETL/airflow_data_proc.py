import os

from airflow import DAG
from airflow.providers.google.cloud.operators.dataproc import(
    DataprocCreateClusterOperator,
    DataprocDeleteClusterOperator,
    DataprocSubmitJobOperator,
)
from airflow.utils.dates import days_ago

PROJECT_ID = 'dataengineeringongcp-400910'
REGION = 'us-east4'
CLUSTER_NAME = 'ephemeral-spark-cluster-{{ ds_nodash }}'
PYSPARK_URI = "gs://deongcp-data-bucket/chapter-5/code/pyspark_job_toBQ.py"

PYSPARK_JOB = {
    "reference": {"project_id": PROJECT_ID},
    "placement": {"cluster_name": CLUSTER_NAME},
    "pyspark_job": {"main_python_file_uri": PYSPARK_URI,
    "jar_file_uris":["gs://spark-lib/bigquery/spark-bigquery-latest_2.12.jar"]
    }
}

cluster_config_json = {
    "worker_config": {
        "num_instances": 2
    }
}

args = {
    'owner': 'gcp-developer'
}

with DAG(
    dag_id='dataproc_ephemeral_cluster_job',
    schedule_interval='0 5 * * *',
    start_date=days_ago(1),
    default_args=args
) as dag:
    create_cluster = DataprocCreateClusterOperator(
        task_id='create_cluster',
        project_id=PROJECT_ID,
        cluster_config=cluster_config_json,
        region='us-east4',
        cluster_name=CLUSTER_NAME,
    )
    
    pyspark_task = DataprocSubmitJobOperator(
        task_id="pyspark_task", job=PYSPARK_JOB, region='us-east4', project_id=PROJECT_ID,
    )
    
    delete_cluster = DataprocDeleteClusterOperator(
        task_id="delete_cluster", project_id=PROJECT_ID, cluster_name=CLUSTER_NAME, region='us-east4',
    )
    
    create_cluster >> pyspark_task >> delete_cluster

if __name__ == "__main__":
    dag.cli()