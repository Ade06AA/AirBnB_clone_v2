#!/usr/bin/python3
"""
module doc
"""

from flask import Flask
app = Flask(__name__)

# app.url_map.strict_slashes = False


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    doc
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
