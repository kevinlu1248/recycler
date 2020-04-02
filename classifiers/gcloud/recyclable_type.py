import io
import os

from google.cloud import vision
from google.cloud.vision import enums
from google.cloud.vision import types
from collections import Counter

print("Connecting API...")
client = vision.ImageAnnotatorClient()

features = [
    types.Feature(type=enums.Feature.Type.OBJECT_LOCALIZATION),
]

requests = []
labels = Counter()


def send_responses():
    response = client.batch_annotate_images(requests)
    for annotation_response in response.responses:
        # print(type(annotation_response.))
        for object in annotation_response.localized_object_annotations:
            # print(object.name)
            labels[object.name] += 1
        # print(annotation_response)


category = "metal"

request = []
labels = Counter()
for i, file_name in enumerate(os.listdir("resources/dataset-resized/{}".format(category))):
    if i % 15 == 14:
        send_responses()
        requests = []
    with io.open("resources/dataset-resized/{}/".format(category) + file_name, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    request = types.AnnotateImageRequest(
        image=image, features=features)
    requests.append(request)

send_responses()
print(labels)
