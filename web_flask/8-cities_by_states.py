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
    st = storage.all(State)
    return render_template("8-cities_by_states.html", storage=st)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
