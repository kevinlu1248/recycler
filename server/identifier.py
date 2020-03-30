import io
import os
import json

from google.cloud import vision
from google.cloud.vision import types
from collections import Counter

with io.open("labels.json", "r") as f:
    LABELS = json.loads(f.read())

client = vision.ImageAnnotatorClient()

file_name = os.path.abspath('src/resources/recyclables_thumb[2].jpg')
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()
image = types.Image(content=content)
response = client.object_localization(image=image)
labels = response.localized_object_annotations

objects = set(label.name for label in labels)

c = Counter()
for label, s in LABELS.items():
    for ob in objects:
        if ob in s:
            c[label] += s[ob]

if not c: print("Sorry, the server is currently full")
print(c)

# C:\Users\XPS\PycharmProjects\recycler\venv\Scripts\python.exe C:/Users/XPS/PycharmProjects/recycler/server/src/gcloud.py
# Connecting API...
# Getting image...
# localizing image...
# Traceback (most recent call last):
#   File "C:\Users\XPS\PycharmProjects\recycler\venv\lib\site-packages\google\api_core\grpc_helpers.py", line 57, in error_remapped_callable
#     return callable_(*args, **kwargs)
#   File "C:\Users\XPS\PycharmProjects\recycler\venv\lib\site-packages\grpc\_channel.py", line 826, in __call__
#     return _end_unary_response_blocking(state, call, False, None)
#   File "C:\Users\XPS\PycharmProjects\recycler\venv\lib\site-packages\grpc\_channel.py", line 729, in _end_unary_response_blocking
#     raise _InactiveRpcError(state)
# grpc._channel._InactiveRpcError: <_InactiveRpcError of RPC that terminated with:
#         status = StatusCode.UNAVAILABLE
#         details = "Getting metadata from plugin failed with error: ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed b
# y the remote host', None, 10054, None))"
#         debug_error_string = "{"created":"@1585553256.568000000","description":"Getting metadata from plugin failed with error: ('Connection aborted.', ConnectionRe
# setError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))","file":"src/core/lib/security/credentials/plugin/plugin_creden
# tials.cc","file_line":79,"grpc_status":14}"
# >
#
# The above exception was the direct cause of the following exception:
#
# Traceback (most recent call last):
#   File "C:/Users/XPS/PycharmProjects/recycler/server/src/gcloud.py", line 18, in <module>
#     response = client.object_localization(image=image)
#   File "C:\Users\XPS\PycharmProjects\recycler\venv\lib\site-packages\google\cloud\vision_helpers\decorators.py", line 101, in inner
#     response = self.annotate_image(request, retry=retry, timeout=timeout)
#   File "C:\Users\XPS\PycharmProjects\recycler\venv\lib\site-packages\google\cloud\vision_helpers\__init__.py", line 72, in annotate_image
#     r = self.batch_annotate_images([request], retry=retry, timeout=timeout)
#   File "C:\Users\XPS\PycharmProjects\recycler\venv\lib\site-packages\google\cloud\vision_v1\gapic\image_annotator_client.py", line 273, in batch_annotate_images
#     return self._inner_api_calls["batch_annotate_images"](
#   File "C:\Users\XPS\PycharmProjects\recycler\venv\lib\site-packages\google\api_core\gapic_v1\method.py", line 143, in __call__
#     return wrapped_func(*args, **kwargs)
#   File "C:\Users\XPS\PycharmProjects\recycler\venv\lib\site-packages\google\api_core\grpc_helpers.py", line 59, in error_remapped_callable
#     six.raise_from(exceptions.from_grpc_error(exc), exc)
#   File "<string>", line 3, in raise_from
# google.api_core.exceptions.ServiceUnavailable: 503 Getting metadata from plugin failed with error: ('Connection aborted.', ConnectionResetError(10054, 'An existing
# connection was forcibly closed by the remote host', None, 10054, None))
#
# Process finished with exit code 1
