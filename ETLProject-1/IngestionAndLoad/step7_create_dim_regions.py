from google.cloud import bigquery

PROJECT_ID = "dataengineeringongcp-400910"
TARGET_TABLE_ID = f"{PROJECT_ID}.dwh_bikesharing.dim_regions"


def create_dim_table(project_id, target_table_id):
    client = bigquery.Client()
    job_config = bigquery.QueryJobConfig(
        destination=target_table_id, write_disposition="WRITE_TRUNCATE"
    )

    sql = f"""
    SELECT CAST(region_id as STRING) as region_id,
    name
    FROM `{project_id}.raw_bikesharing.regions`
    """

    query_job = client.query(sql, job_config=job_config)

    try:
        query_job.result()
        print("Query Success")
    except Exception as exception:
        print(exception)


if __name__ == "__main__":
    create_dim_table(PROJECT_ID, TARGET_TABLE_ID)
