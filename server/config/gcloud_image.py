import io
import os
import json
import config
from google.cloud import vision
from google.cloud.vision import types
from collections import Counter
module_path = os.path.dirname(config.__file__)
with io.open(module_path + "/labels.json", "r") as f:
    LABELS = json.loads(f.read())

client = vision.ImageAnnotatorClient()