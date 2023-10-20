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


if __name__ == "__main__":
    app.run()
