from google.cloud import bigquery

GCP_PROJECT_ID = "dataengineeringongcp-400910"
GCP_GCS_URL = "gs://deongcp-data-bucket/mysql_exports/stations/20180102/stations.csv"
GCP_DATASET_ID = "dataengineeringongcp-400910.raw_bikesharing"
GCP_TABLE_ID = f"{GCP_PROJECT_ID}.raw_bikesharing.stations"


def merge_gcs_to_bigquery_incremental(TABLE_ID, DATASET_ID, PROJECT_ID, GCS_URL):
    client = bigquery.Client()

    merge_sql = f"""
    
    MERGE `{TABLE_ID}` as target
    USING `{GCS_URL}` as source
    on target.station_id = source.station_id
    WHEN MATCHED THEN
        UPDATE SET target.station_id = source.station_id, target.name = source.name, target.region_id = source.region_id, target.capacity = source.capacity
    WHEN NOT MATCHED THEN
        INSERT (station_id, name, region_id, capacity)
        VALUES (source.station_id, source.name, source.region_id, source.capacity)
    """
    query_job = client.query(merge_sql)
    try:
        query_job.result()
        print("UPSERT Successfull")
    except Exception as exception:
        print(exception)


if __name__ == "__main__":
    merge_gcs_to_bigquery_incremental(
        GCP_TABLE_ID, GCP_DATASET_ID, GCP_PROJECT_ID, GCP_GCS_URL
    )
