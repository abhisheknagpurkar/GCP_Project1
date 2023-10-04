gcloud sql instances create mysql-instance-source  \
--database-version=MYSQL_5_7 \
--tier=db-g1-small \
--region=us-east4 \
--root-password=dbadmin123 \
--availability-type=zonal \
--storage-size=10GB \
--storage-type=HDD