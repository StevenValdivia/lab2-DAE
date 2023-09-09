#!/usr/bin/env python

from flask import Flask
from flask import jsonify
from linkextractor import extract_links

app = Flask(__name__)

@app.route("/")
def index():
    return "Usage: http://<hostname>[:<prt>]/api"

@app.route("/api")
def api():
    links = extract_links()
    return jsonify(links)

app.run(host="0.0.0.0")
