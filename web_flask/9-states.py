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


@app.route("/states", defaults={'id': None}, strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states(id):
    """ script that starts a Flask web application
    """

    states = storage.all(State)
    data = {"states": None, "state": None}

    if id is None:
        sorted_states = sorted(storage.all(State).values(),
                               key=lambda state: state.name)
        data["states"] = sorted_states
        return render_template("9-states.html", data=data)

    # check if id is valid
    if not states.get("State.{}".format(id)):
        return render_template("9-states.html", data=data)

    state = states.get("State.{}".format(id))
    data["state"] = state
    return render_template("9-states.html", data=data)


@app.teardown_appcontext
def teardown_db(exception):
    """ remove the current SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
