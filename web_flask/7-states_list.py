#!/usr/bin/python3
from flask import Flask, render_template
from sys import path

path.append('..')
from models import storage
from models.state import State

"""
module doc
"""

app = Flask(__name__)

app.url_map.strict_slashes = False

@app.teardown_appcontext
def after_every_request7(f):
    """
    doc
    """
    storage.close()

@app.route("/states_list")
def next6():
    """
    doc
    """
    return render_template("7-states_list.html", storage=storage.all(State))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
