#!/usr/bin/python3
"""
starts flask web application
listens on 0.0.0.0, port 5000
"""
from flask import flask

app = Flask(__name__)


@app.route('/', strict_flashes=False)
def hello_hbnb():
    """returns the string (Hello, HBNB!)"""
    return ('Hello, HBNB!')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)