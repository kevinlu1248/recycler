import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

print("Connecting API...")
client = vision.ImageAnnotatorClient()

print("Getting image...")
file_name = os.path.abspath('resources/recyclables_thumb[2].jpg')
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()
image = types.Image(content=content)

print("localizing image...")
response = client.object_localization(image=image)
labels = response.localized_object_annotations

print('Names:')
for label in labels:
    print(label.name)

print("Labelling image....")
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label)

# set GOOGLE_APPLICATION_CREDENTIALS="C:\Users\XPS\Recycler-f84417bf5f6d.json"