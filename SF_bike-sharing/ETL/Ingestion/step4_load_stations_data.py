from google.cloud import bigquery

# TODO : Change to your project id
GCP_PROJECT_ID = "dataengineeringongcp-400910"
GCP_TABLE_ID = "{}.raw_bikesharing.stations".format(GCP_PROJECT_ID)
GCP_GCS_URI = "gs://deongcp-data-bucket/mysql_exports/stations/20180102/stations.csv"


def load_gcs_to_bigquery_snapshot_data(GCS_URI, TABLE_ID, table_schema):
    client = bigquery.Client()
    job_config = bigquery.LoadJobConfig(
        schema=table_schema,
        source_format=bigquery.SourceFormat.CSV,
        write_disposition="WRITE_TRUNCATE",
    )

    load_job = client.load_table_from_uri(GCS_URI, TABLE_ID, job_config=job_config)
    load_job.result()
    table = client.get_table(TABLE_ID)

    print("Loaded {} rows to table {}".format(table.num_rows, TABLE_ID))


bigquery_table_schema = [
    bigquery.SchemaField("station_id", "STRING"),
    bigquery.SchemaField("name", "STRING"),
    bigquery.SchemaField("region_id", "STRING"),
    bigquery.SchemaField("capacity", "INTEGER"),
]

if __name__ == "__main__":
    load_gcs_to_bigquery_snapshot_data(GCP_GCS_URI, GCP_TABLE_ID, bigquery_table_schema)
