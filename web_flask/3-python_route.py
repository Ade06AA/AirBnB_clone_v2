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


@app.route("/c/<text>")
def next2(text):
    """
    doc
    """
    return f"C {text.replace('_', ' ')}"


@app.route("/python")
@app.route("/python/<text>")
def next3(text="is cool"):
    """
    doc
    """
    return f"Python {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
