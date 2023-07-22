#!/usr/bin/python3
"""Starts flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Returns the string Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns the string when the url contains(/hbnb)"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
