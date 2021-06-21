# app.py

import os
import json
import classifiers
from classifiers.identifier import predict_from_binary
from flask import Flask, Response, render_template, send_file, request

# Initialize Flask App
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "tmp"
accepted_image_types = {
    "jpeg",
    "png",
    "gif",
    "bmp",
    "raw",
    "ico",
    "pdf",
    "tiff",
}

@app.route('/')
def index():
    app.logger.info("GET /".format())
    return render_template("frontend.html")


@app.route('/classify', methods=['POST'])
def classify():
    # TODO: error management (https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/)
    app.logger.info("Got image to /classify")

    file = request.files['image']
    _, ext = os.path.splitext(file.filename)
    blob = file.read()

    results = predict_from_binary(blob)
    print(results)
    return Response(response=results, status=200, mimetype="application/json")


port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
