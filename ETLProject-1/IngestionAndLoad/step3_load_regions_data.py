from google.cloud import bigquery

GCP_PROJECT_ID = "dataengineeringongcp-400910"
GCP_PUBLIC_TABLE_ID = "bigquery-public-data.san_francisco_bikeshare.bikeshare_regions"
GCP_TARGET_TABLE_ID = f"{GCP_PROJECT_ID}.raw_bikesharing.regions"


def load_data_from_bigquery_public(PUBLIC_TABLE_ID, TARGET_TABLE_ID):
    client = bigquery.Client()

    job_config = bigquery.QueryJobConfig(
        destination=TARGET_TABLE_ID, write_disposition="WRITE_TRUNCATE"
    )

    sql = f"Select * from {PUBLIC_TABLE_ID}"
    query_job = client.query(sql, job_config=job_config)
    try:
        query_job.result()
        print("Load Successful")
    except Exception as exception:
        print(exception)


if __name__ == "__main__":
    load_data_from_bigquery_public(GCP_PUBLIC_TABLE_ID, GCP_TARGET_TABLE_ID)
