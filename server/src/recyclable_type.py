import io
import os

from google.cloud import vision
from google.cloud.vision import enums
from google.cloud.vision import types

print("Connecting API...")
client = vision.ImageAnnotatorClient()

features = [
    types.Feature(type=enums.Feature.Type.OBJECT_LOCALIZATION),
]

requests = []

def send_responses():
    response = client.batch_annotate_images(requests)
    for annotation_response in response.responses:
        print(annotation_response)

for i, file_name in enumerate(os.listdir("resources/dataset-resized/cardboard")):
    if i % 17 == 16:
        send_responses()
        requests = []
    with io.open("resources/dataset-resized/cardboard/" + file_name, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    request = types.AnnotateImageRequest(
        image=image, features=features)
    requests.append(request)

send_responses()

# object_labels = set()
# for file_name in os.listdir("resources/dataset-resized/cardboard"):
#     # print("Getting image..")
#     with io.open("resources/dataset-resized/cardboard/" + file_name, 'rb') as image_file:
#         content = image_file.read()
#     image = types.Image(content=content)
#
#     # print("localizing image...")
#     response = client.object_localization(image=image)
#     labels = response.localized_object_annotations
#     # print(response)
#
#     for label in labels:
#         object_labels.add(label.name)
#         print(file_name + ": " + label.name)
#
# print(object_labels)