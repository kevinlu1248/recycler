# app.py
# Required Imports
import os
import logging
from flask import Flask, Response, render_template, send_from_directory, send_file

# Initialize Flask App
app = Flask(__name__, static_folder="../static")


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
    return Response(response="It went through!", status=200)


port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
