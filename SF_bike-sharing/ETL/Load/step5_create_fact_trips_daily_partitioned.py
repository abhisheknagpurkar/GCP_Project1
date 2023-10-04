import sys
from google.cloud import bigquery

PROJECT_ID = "dataengineeringongcp-400910"
TARGET_TABLE_ID = f"{PROJECT_ID}.dwh_bikesharing.fact_trips_daily"

def create_fact_table(project_id, target_table_id):
    client = bigquery.Client()

    # Step 1: Create the table with partitioning using DDL (Data Definition Language)
    table_schema = [
        bigquery.SchemaField("trip_date", "DATE"),
        bigquery.SchemaField("start_station_id", "STRING"),
        bigquery.SchemaField("total_trips", "INTEGER"),
        bigquery.SchemaField("sum_duration_sec", "INTEGER"),
        bigquery.SchemaField("avg_duration_sec", "FLOAT"),
    ]

    table_ref = client.dataset("dwh_bikesharing").table("fact_trips_daily")
    table = bigquery.Table(table_ref, schema=table_schema)

    # Define partitioning options
    partitioning = bigquery.TimePartitioning(
        type_=bigquery.TimePartitioningType.DAY,
        field="trip_date",
    )
    table.time_partitioning = partitioning

    try:
        client.create_table(table)
        print(f"Table {target_table_id} created successfully")
    except Exception as exception:
        print(exception)

if __name__ == "__main__":
    create_fact_table(PROJECT_ID, TARGET_TABLE_ID)