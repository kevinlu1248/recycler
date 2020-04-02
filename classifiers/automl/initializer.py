# DATASET_ID=ICN3650956947332530176

from google.cloud import automl

# TODO(developer): Uncomment and set the following variables
project_id = "recycler-7dc49"
display_name = "flowers"

client = automl.AutoMlClient()

# A resource that represents Google Cloud Platform location.
project_location = client.location_path(project_id, "us-central1")
# Specify the classification type
# Types:
# MultiLabel: Multiple labels are allowed for one example.
# MultiClass: At most one label is allowed per example.
# https://cloud.google.com/automl/docs/reference/rpc/google.cloud.automl.v1#classificationtype
metadata = automl.types.ImageClassificationDatasetMetadata(
    classification_type=automl.enums.ClassificationType.MULTICLASS
)
dataset = automl.types.Dataset(
    display_name=display_name,
    image_classification_dataset_metadata=metadata,
)

# Create a dataset with the dataset metadata in the region.
response = client.create_dataset(project_location, dataset)

created_dataset = response.result()

# Display the dataset information
print("Dataset name: {}".format(created_dataset.name))
print("Dataset id: {}".format(created_dataset.name.split("/")[-1]))
