#!/usr/bin/python3
""" module for Flask web application
"""
from flask import Flask
from flask import render_template

from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", defaults={"state_id": None}, strict_slashes=False)
@app.route("/states/<state_id>", strict_slashes=False)
def state_by_id(state_id):
    """ get state by id:
        Args:
             state_id: state id
    """
    data = {}
    states = storage.all(State)

    if state_id is None:
        sorted_states = sorted(storage.all(State).values(),
                               key=lambda state: state.name)
        data["states"] = sorted_states
        return render_template("9-states.html", data=data)

    # check if id is valid
    if states.get("State.{}".format(state_id)) is None:
        return render_template("9-states.html", data=None)

    data["state"] = states.get("State.{}".format(state_id))
    return render_template("9-states.html", data=data)


@app.teardown_appcontext
def teardown_db(exception):
    """ remove the current SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
