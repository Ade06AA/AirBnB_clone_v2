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


@app.route("/states")
@app.route("/states/<Id>")
def next6(Id=None):
    """
    doc
    """
    # if i use storage as a local variable instead of storage_
    # it is going to asume the storage in storage.all(state) is also
    # a local variable from the function even if it comes before the
    # asignment of the new storage variable if i were to use the same name
    storage_ = storage.all(State)
    # when function sorted is called on a dict it only consider the
    # keys of the dict and return only a list of the sorted key
    sorted_key = sorted(storage_, key=lambda x: storage_[x].name)
    storage_ = {k: storage_[k] for k in sorted_key}
    return render_template("9-states.html", storage=storage_, Id=Id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
