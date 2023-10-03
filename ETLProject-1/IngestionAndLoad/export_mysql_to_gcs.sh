bucket_name=deongcp-data-bucket
gcloud sql export csv mysql-data-source \
gs://$bucket_name/mysql_exports/stations/20180101/stations.csv \
--database=apps_db \
--offload \
--query='Select * from stations where station_id < 200;'
gcloud sql export csv mysql-data-source \
gs://$bucket_name/mysql_exports/stations/20180102/stations.csv \
--database=apps_db \
--offload \
--query='Select * from stations where station_id < 400;'