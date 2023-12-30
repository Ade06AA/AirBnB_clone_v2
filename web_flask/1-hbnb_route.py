#!/usr/bin/python3
from flask import Flask

"""
module doc
"""

app = Flask(__name__)

app.url_map.strict_slashes = False

@app.route("/")
def home():
    """
    doc
    """
    return "Hello HBNB!"

@app.route("/hbnb")
def next():
    """
    doc
    """
    return "HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
