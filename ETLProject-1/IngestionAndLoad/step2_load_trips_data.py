from google.cloud import bigquery

GCP_PROJECT_ID = "dataengineeringongcp-400910"
GCP_GCS_URL = (
    "gs://deongcp-data-bucket/from-git/chapter-3/dataset/trips/20180101/*.json"
)
GCP_TABLE_ID = f"{GCP_PROJECT_ID}.raw_bikesharing.trips"

client = bigquery.Client()


def load_gcs_to_bigquery(GCS_URL, TABLE_ID, table_schema):
    job_config = bigquery.LoadJobConfig(
        schema=table_schema,
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
        write_disposition="WRITE_APPEND",
    )

    load_job = client.load_table_from_uri(GCS_URL, TABLE_ID, job_config=job_config)

    load_job.result()
    table = client.get_table(TABLE_ID)

    print(f"Loaded {table.num_rows} rows to table {TABLE_ID}")


bigquery_table_schema = [
    bigquery.SchemaField("trip_id", "STRING"),
    bigquery.SchemaField("duration_sec", "INTEGER"),
    bigquery.SchemaField("start_date", "TIMESTAMP"),
    bigquery.SchemaField("start_station_name", "STRING"),
    bigquery.SchemaField("start_station_id", "STRING"),
    bigquery.SchemaField("end_date", "TIMESTAMP"),
    bigquery.SchemaField("end_station_name", "STRING"),
    bigquery.SchemaField("end_station_id", "STRING"),
    bigquery.SchemaField("member_gender", "STRING"),
]

if __name__ == "__main__":
    load_gcs_to_bigquery(GCP_GCS_URL, GCP_TABLE_ID, bigquery_table_schema)
