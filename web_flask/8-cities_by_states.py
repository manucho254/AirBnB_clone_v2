#!/usr/bin/python3
""" module for Flask web application
"""
from flask import Flask
from flask import render_template

from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def state_cities():
    """
       list state and all cities related to the state:
    """

    states = sorted(storage.all(State).values(),
                    key=lambda state: state.name)

    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def tear_down(exception):
    """
       remove the current SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
