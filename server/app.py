# app.py
# Required Imports
import os
import json
from config import gcloud_storage
from server.classifiers.gcloud import identifier
from flask import Flask, Response, render_template, send_file, request

# Initialize Flask App
app = Flask(__name__, static_folder="../static")
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
    # app.logger.info(url_for('static', filename='img/favicon.ico'))
    return render_template("frontend.html")


@app.route('/static/<path:path>')
def send_js(path):
    app.logger.info("Call to /static/{}".format(path))
    app.logger.info(send_file("..\\static\\" + path))
    return send_file("..\\static\\" + path)


@app.route('/classify', methods=['POST'])
def classify():
    # form = request.form['submit']
    # TODO: error management (https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/)
    app.logger.info("Got image to /classify")

    file = request.files['image']
    _, ext = os.path.splitext(file.filename)
    blob = file.read()
    gcloud_storage.push_blob_from_string(blob, ext)
    results = identifier.identify_from_string(blob)
    print(results)
    return Response(response=results, status=200, mimetype="application/json")


port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
