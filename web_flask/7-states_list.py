#!/usr/bin/python3
"""
module doc
"""

from flask import Flask, render_template
from sys import path
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
def next6():
    """
    doc
    """
    st = storage.all(State).values()
    st = sorted(st, key=lambda x: x.name)
    return render_template("7-states_list.html", storage=st)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
