#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 YA-androidapp(https://github.com/YA-androidapp) All rights reserved.

# py -m venv myenv
# /myenv/Scripts/Activate.ps1
# python -m pip install flask
# python .\serve.py

import os
from flask import Flask, jsonify, make_response, redirect, render_template, request, send_from_directory


app = Flask(__name__, template_folder=".")
app.config['MAX_CONTENT_LENGTH'] = 100*1024*1024


UPLOAD_FOLDER = "./uploads/"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    if ("file" in request.files):
        file = request.files["file"]
        # file.save(os.path.join(UPLOAD_FOLDER ,file.filename))
        blob = request.files['file'].read()
        size = len(blob)
        return make_response(jsonify({'size': size}))
    return make_response(jsonify({'size': -1}))


@app.route("/img")
def file_view():
    return send_from_directory(".", 'check.png')


if __name__ == '__main__':
    app.run(debug=True)
