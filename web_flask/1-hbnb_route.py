#!/usr/bin/python3
""" module for Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """ script that starts a Flask web application:
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ path to display “HBNB”
    """
    return "HBNB"


if __name__ == "__main__":
    app.run()
