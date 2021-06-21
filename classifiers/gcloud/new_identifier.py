# import tensorflow as tf
from tensorflow import keras
import json
import numpy as np
from numpy import asarray
from PIL import Image
from io import BytesIO
# import cv2

classes = ["cardboard", "glass", "metal", "paper", "plastic", "trash"]
model = keras.models.load_model('classifiers/gcloud/xception_256.h5')

def predict_from_binary(b):
	# print(type(b))
	image = Image.open(BytesIO(b))
	image = image.resize((256, 256))
	
	data = np.array([asarray(image) / 255.])
	
	if data.shape[-1] == 4:
		data = data[:,:,:,:3]
	# print(data.shape)
	# print(model.predict([data]))
	prediction = model.predict(data)
	class_name = model.predict_classes(data)
	print(prediction)
	print(class_name)
	print(max(prediction[0].tolist()))
	print(type(max(prediction[0].tolist())))

	result = {
        "classification": {
            "name": classes[class_name[0]],
            "confidence": max(prediction[0].tolist())
        },
        "success": True,

    }
	return json.dumps(result)

if __name__ == '__main__':
	# model.summary()
	# image = Image.open("../../resources/dataset-resized/cardboard/cardboard1.jpg")
	# print(predict_from_binary())
	test_image = ""
	with open('../../resources/dataset-resized/cardboard/cardboard1.jpg', 'rb') as f:
		test_image = f.read()
	print(len(test_image))
	print(predict_from_binary(test_image))
