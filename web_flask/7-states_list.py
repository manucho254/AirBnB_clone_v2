#!/usr/bin/python3
""" module for Flask web application
"""
from flask import Flask
from flask import render_template

from models import storage
from models.state import State

import sys
sys.path.append("../")

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states():
    """ script that starts a Flask web application:
    """

    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """ remove the current SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
