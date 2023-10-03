from google.cloud import bigquery
from google.cloud.exceptions import NotFound

client = bigquery.Client()

datasets_name = [
    "raw_bikesharing",
    "dwh_bikesharing",
    "dm_regional_manager",
    "dm_bikesharing",
]
location = "us-east4"


def create_bigquery_dataset(dataset_name):
    """Create bigquery dataset, check if one already exists
    Args:
        datasets_name: String"""
    dataset_id = f"{client.project}.{dataset_name}"
    try:
        client.get_dataset(dataset_id)
        print(f"Dataset {dataset_id} already exists")
    except NotFound:
        dataset = bigquery.Dataset(dataset_id)
        dataset.location = location
        dataset = client.create_dataset(dataset, timeout=30)
        print(f"Created dataset {client.project}.{dataset.dataset_id}")


for name in datasets_name:
    create_bigquery_dataset(name)
