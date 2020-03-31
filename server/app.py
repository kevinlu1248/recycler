# app.py
# Required Imports
import os
from config import gcloud_storage
from classifiers.gcloud import identifier
import google.cloud
from flask import Flask, Response, render_template, send_from_directory, send_file, request, redirect, url_for
from werkzeug.utils import secure_filename

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
    return render_template("index.html")


@app.route('/static/<path:path>')
def send_js(path):
    app.logger.info("Call to /static/{}".format(path))
    app.logger.info(send_file(send_file("..\\static\\" + path)))
    return send_file("..\\static\\" + path)


@app.route('/classify', methods=['POST'])
def classify():
    # form = request.form['submit']
    # TODO: error management (https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/)
    app.logger.info("Got image to /classify")

    file = request.files['image']
    _, ext = os.path.splitext(file.filename)
    gcloud_storage.push_blob_from_string(file.read(), ext)

    return Response(response="It went through!", status=200)


port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
