# app.py
# Required Imports
# recycler-7dc49
import os
import json
from config import gcloud_storage
from classifiers.automl import classifier
from classifiers.gcloud import identifier
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


# @app.route('/static/<path:path>')
# def send_js(path):
#     app.logger.info("Call to /static/{}".format(path))
#     app.logger.info(send_file("..\\static\\" + path))
#     return send_file("..\\static\\" + path)


@app.route('/classify', methods=['POST'])
def classify():
    # form = request.form['submit']
    # TODO: error management (https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/)
    app.logger.info("Got image to /classify")

    file = request.files['image']
    _, ext = os.path.splitext(file.filename)
    blob = file.read()
    gcloud_storage.push_blob_from_string(blob, ext)
    # results = identifier.identify_from_string(blob)
    results = classifier.get_prediction(blob)
    print(results)
    return Response(response=results, status=200, mimetype="application/json")


port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)

# gcloud projects add-iam-policy-binding recycler-7dc49 --member="serviceAccount:service-998017231527@gcp-sa-automl.iam.gserviceaccount.com" --role="roles/storage.admin"
# gsutil mb -p recycler-7dc49 -c regional -l us-central1 gs://recycler-7dc49-vcm/
# set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\XPS\Recycler-f84417bf5f6d.json
# gsutil -m cp -R gs://cloud-ml-data/img/flower_photos/  gs://recycler-7dc49-vcm/img/
# gsutil cat gs://recycler-7dc49-vcm/img/flower_photos/all_data.csv | sed "s:cloud-ml-data:recycler-7dc49-vcm:" > all_data.csv
# gsutil cp all_data.csv gs://recycler-7dc49-vcm/csv/