from google.cloud import automl
import os

# TODO(developer): Uncomment and set the following variables
project_id = "recycler-7dc49"
display_name = "flowers"
path = "gs://recycler-7dc49-vcm/csv/all_data.csv"

client = automl.AutoMlClient()
# Get the full path of the dataset.
dataset_full_id = client.dataset_path(
    project_id, "us-central1", os.environ.get("DATASET_ID")
)
# Get the multiple Google Cloud Storage URIs
input_uris = path.split(",")
gcs_source = automl.types.GcsSource(input_uris=input_uris)
input_config = automl.types.InputConfig(gcs_source=gcs_source)
# Import data from the input URI
response = client.import_data(dataset_full_id, input_config)

print("Processing import...")
print("Data imported. {}".format(response.result()))