from google.cloud import bigquery

PROJECT_ID = "dataengineeringongcp-400910"
TARGET_TABLE_ID = f"{PROJECT_ID}.dwh_bikesharing.dim_stations"


def create_dim_table(project_id, target_table_id):
    client = bigquery.Client()
    job_config = bigquery.QueryJobConfig(
        destination=target_table_id, write_disposition="WRITE_TRUNCATE"
    )

    sql = f"""
    SELECT station_id,
    stations.name as station_name,
    regions.name as region_name,
    capacity
    FROM `{project_id}.raw_bikesharing.stations` as stations
    JOIN `{project_id}.raw_bikesharing.regions` as regions
    ON stations.region_id = CAST(regions.region_id AS STRING)
    """

    query_job = client.query(sql, job_config=job_config)

    try:
        query_job.result()
        print("Query Successful")
    except Exception as exception:
        print(exception)


if __name__ == "__main__":
    create_dim_table(PROJECT_ID, TARGET_TABLE_ID)
