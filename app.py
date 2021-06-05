from sketchify import sketch
import imghdr
import os
from flask import Flask, render_template, request, redirect, url_for,send_file, abort, \
    send_from_directory
from werkzeug.utils import secure_filename
import zipfile
import cv2

app = Flask(__name__)

PORT = 3000

app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = '.'

@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('index.html', files=files)

@app.route('/', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], "raw.png"))
    return '', 204

@app.route("/result")
def startpy():
    sketch.normalsketch('raw.png',
    'static/images','mothdraw2')

    return render_template("index_old.html", result = "mothdraw2")

@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=PORT)