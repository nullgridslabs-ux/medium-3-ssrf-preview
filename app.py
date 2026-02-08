# medium-3-ssrf-preview/app.py
from flask import Flask, request
import requests
import os

app = Flask(__name__)
FLAG = os.environ.get("FLAG","CTF{dev}")

@app.route("/")
def index():
    return """
<h2>Remote Content Preview</h2>
<ul>
<li>POST /preview</li>
<li>GET /metadata</li>
<li>GET /health</li>
</ul>
"""

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
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
