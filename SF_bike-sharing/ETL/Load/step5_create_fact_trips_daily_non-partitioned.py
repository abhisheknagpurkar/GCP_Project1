import sys
from google.cloud import bigquery

PROJECT_ID = "dataengineeringongcp-400910"
TARGET_TABLE_ID = f"{PROJECT_ID}.dwh_bikesharing.fact_trips_daily"


def create_fact_table(project_id, target_table_id):
    load_date = sys.argv[1]  # date format: yyyy-mm-dd
    print(f"Load Date : {load_date}")

    client = bigquery.Client()
    job_config = bigquery.QueryJobConfig(
        destination=target_table_id, write_disposition="WRITE_APPEND"
    )

    sql = f"""
    CREATE TABLE {target_table_id}
    partition by trip_date
    AS (
    select DATE(start_date) as trip_date,
    start_station_id,
    COUNT(trip_id) as total_trips,
    SUM(duration_sec) as sum_duration_sec,
    AVG(duration_sec) as avg_duration_sec
    FROM `{project_id}.raw_bikesharing.trips` trips
    JOIN `{project_id}.raw_bikesharing.stations` stations
    ON trips.start_station_id = stations.station_id
    WHERE DATE(start_date) =  DATE('{load_date}')
    GROUP BY trip_date, start_station_id
    )
    """
    query_job = client.query(sql, job_config=job_config)

    try:
        query_job.result()
        print("Query Success")
    except Exception as exception:
        print(exception)


if __name__ == "__main__":
    create_fact_table(PROJECT_ID, TARGET_TABLE_ID)
