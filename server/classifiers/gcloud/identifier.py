import io
import os
import json
# import config
from google.cloud import vision
from google.cloud.vision import types
from collections import Counter

client = vision.ImageAnnotatorClient()
TYPES = ["paper", "cardboard", "glass", "metal", "plastic", "trash"]

with io.open("config/labels.json", "r") as f:
    LABELS = json.loads(f.read())


def identify_from_string(blob):
    image = types.Image(content=blob)
    response = client.object_localization(image=image)
    labels = response.localized_object_annotations
    objects = set(label.name for label in labels)

    c = Counter()
    for label, s in LABELS.items():
        for ob in objects:
            if ob in s:
                c[label] += s[ob]

    if not c: print("Sorry, the server is currently full.")

    # Laplace rule of succession
    sm = sum(c[k] + 1 for k in c)
    mx = max(c, key=lambda k: c[k])
    normalized = {t: (c[t] + 1) / sm for t in TYPES}
    results = {
        "success": bool(c),
        "raw": dict(c),
        "normalized": normalized,
        "classification": {
            "name": mx,
            "confidence": (c[mx] + 1) / sm
        }
    }

    return json.dumps(results)


if __name__ == '__main__':
    c = Counter({"cardboard": 13, "metal": 15, "paper": 144, "plastic": 2, "trash": 11})
    # Laplace rule of succession
    sm = sum(c[k] + 1 for k in c)
    mx = max(c, key=lambda k: c[k])
    normalized = {t: (c[t] + 1) / sm for t in TYPES}
    results = {
        "success": bool(c),
        "raw": dict(c),
        "normalized": normalized,
        "classification": {
            "name": mx,
            "confidence": (c[mx] + 1) / sm
        }
    }
    print(json.dumps(results))
