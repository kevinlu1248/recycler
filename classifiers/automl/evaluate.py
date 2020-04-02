from google.cloud import automl

project_id = "recycler-7dc49"
model_id = "ICN7596899670257827840"

client = automl.AutoMlClient()
# Get the full path of the model.
model_full_id = client.model_path(project_id, "us-central1", model_id)

print("List of model evaluations:")
for evaluation in client.list_model_evaluations(model_full_id, ""):
    print("Model evaluation name: {}".format(evaluation.name))
    print(
        "Model annotation spec id: {}".format(
            evaluation.annotation_spec_id
        )
    )
    print("Create Time:")
    print("\tseconds: {}".format(evaluation.create_time.seconds))
    print("\tnanos: {}".format(evaluation.create_time.nanos / 1e9))
    print(
        "Evaluation example count: {}".format(
            evaluation.evaluated_example_count
        )
    )
    print(
        "Classification model evaluation metrics: {}".format(
            evaluation.classification_evaluation_metrics
        )
    )