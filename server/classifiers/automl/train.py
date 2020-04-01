import os

from google.cloud import automl

# TODO(developer): Uncomment and set the following variables
project_id = "recycler-7dc49"
display_name = "flowers"
path = "gs://recycler-7dc49-vcm/img/flower_photos/train_set.csv"
display_name = "flowers_model"
dataset_id = os.environ.get("DATASET_ID")

client = automl.AutoMlClient()

# A resource that represents Google Cloud Platform location.
project_location = client.location_path(project_id, "us-central1")
# Leave model unset to use the default base model provided by Google
# train_budget_milli_node_hours: The actual train_cost will be equal or
# less than this value.
# https://cloud.google.com/automl/docs/reference/rpc/google.cloud.automl.v1#imageclassificationmodelmetadata
metadata = automl.types.ImageClassificationModelMetadata(
    train_budget_milli_node_hours=24000
)
model = automl.types.Model(
    display_name=display_name,
    dataset_id=dataset_id,
    image_classification_model_metadata=metadata,
)

# Create a model with the model metadata in the region.
response = client.create_model(project_location, model)

print("Training operation name: {}".format(response.operation.name))
print("Training started...")