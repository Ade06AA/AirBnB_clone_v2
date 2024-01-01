#!/usr/bin/python3
"""
module doc
"""

from flask import Flask, render_template
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


@app.route("/number/<int:n>")
def next4(n):
    """
    doc
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def next5(n):
    """
    doc
    """
    return render_template("5-number.html", num=n)


@app.route("/number_odd_or_even/<int:n>")
def next6(n):
    """
    doc
    """
    return render_template("6-number_odd_or_even.html", num=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
