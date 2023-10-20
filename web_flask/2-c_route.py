#!/usr/bin/python3
""" module for Flask web application
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def route_1():
    """ script that starts a Flask web application:
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def route_2():
    """ path to display “HBNB”
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def route_3(text):
    """ display “C ” followed by the value of the text
    """
    value = escape(text).replace("_", " ")

    return "C {}".format(value)


if __name__ == "__main__":
    app.run()
