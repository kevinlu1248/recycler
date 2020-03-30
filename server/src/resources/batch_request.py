import io
import os

from google.cloud import vision
from google.cloud.vision import enums
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()

features = [
    types.Feature(type=enums.Feature.Type.OBJECT_LOCALIZATION),
]

requests = []
for i, file_name in enumerate(os.listdir("resources/dataset-resized/cardboard")):
    if i == 16: break
    with io.open("resources/dataset-resized/cardboard/" + file_name, 'rb') as image_file:
        print("copying image " + file_name)
        content = image_file.read()
    image = types.Image(content=content)
    request = types.AnnotateImageRequest(
        image=image, features=features)
    requests.append(request)

response = client.batch_annotate_images(requests)

for annotation_response in response.responses:
    print(annotation_response)
