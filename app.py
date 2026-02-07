# medium-3-ssrf-preview/app.py
from flask import Flask, request
import requests
import os

app = Flask(__name__)
FLAG = os.environ.get("FLAG","CTF{dev}")

@app.route("/health")
def health():
    return "ok"

@app.route("/metadata")
def meta():
    return FLAG

@app.route("/preview", methods=["POST"])
def preview():
    url = request.json.get("url")
    r = requests.get(url, timeout=3)
    return r.text

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
