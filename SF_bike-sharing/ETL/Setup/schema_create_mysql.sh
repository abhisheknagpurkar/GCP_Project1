
gcloud sql connect mysql-instance-source --user=root

CREATE DATABASE apps_db;

CREATE TABLE apps_db.stations(
station_id varchar(255),
name varchar(255),
region_id varchar(10),
capacity integer
);
