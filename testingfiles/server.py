from flask import Flask, request, Response
from flask_cors import CORS, cross_origin
import urllib.request
import json


UPLOAD_FOLDER = 'uploads/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CORS_HEADERS'] = 'Content-Type'

CORS(app)

@app.route("/", methods=["GET"])
def index():
    return "Hello World !"

@app.route("/upload", methods=["GET", "POST"])
@cross_origin()
def upload():
    if request.method == "POST":
        if "file_attachment" in request.form:
            image_url = request.form.get("file_attachment")
            save_name = 'nacho.wav' 
            urllib.request.urlretrieve(image_url, "{0}{1}".format(app.config['UPLOAD_FOLDER'], save_name))
            return json.dumps({ "status" : True})
        else:
            return "No file found !"
    else:
        return "File uploader active !"