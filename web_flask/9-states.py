#!/usr/bin/python3
"""
module doc
"""

from flask import Flask, render_template
from sys import path
path.append('..')
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
    st = storage.all(State)
    print(st["State.421a55f4-7d82-47d9-b54c-a76916479545"])
    return render_template("9-states.html", storage=st, Id=Id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
