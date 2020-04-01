import json

from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.proto import service_pb2


# 'content' is base-64-encoded image data.
def get_prediction(content):
    project_id = "998017231527"
    model_id = "ICN2836313389150502912"

    prediction_client = automl_v1beta1.PredictionServiceClient()

    name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
    payload = {'image': {'image_bytes': content}}
    params = {}
    request = prediction_client.predict(name, payload, params)
    # print(request)
    result = {
        "classification": {
            "name": request.payload[0].display_name,
            "confidence": request.payload[0].classification.score
        },
        "success": True,

    }
    return json.dumps(result)  # waits till request is returned


if __name__ == '__main__':
    file_path = "classifiers/automl/tulip-divisions.jpg"
    with open(file_path, 'rb') as ff:
        content = ff.read()
    print(get_prediction(content))
