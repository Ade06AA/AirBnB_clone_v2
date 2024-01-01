#!/usr/bin/python3
"""
module doc
"""

from flask import Flask, render_template
from sys import path
# path.append('..')
from models import storage
from models.state import State

app = Flask(__name__)

app.url_map.strict_slashes = False


@app.teardown_appcontext
def after_every_request7(f):
    """
    doc
    """
    storage.close()


@app.route("/states_list")
@app.route("/states_list/<Id>")
def next6(Id=None):
    """
    doc
    """
    storage = storage.all(State)
    # when function sorted is called on a dict it only consider the
    # keys of the dict and return only a list of the sorted key
    sorted_key = sorted(storage, key=lambda x: storage[x].name)
    storage = {k: storage[k] for k in sorted_key}
    return render_template("9-states.html", storage=storage, Id=Id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
