#!/usr/bin/python3
""" module for Flask web application
"""
from flask import Flask
from flask import render_template

from models import storage
from models.state import State

app = Flask(__name__)

storage.reload()  # Reload objects
states = storage.all(State)  # Get all states

print(states)

@app.teardown_appcontext
def teardown_db(exception):
    """ remove the current SQLAlchemy Session
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def status_list():
    """ script that starts a Flask web application:
    """

    return render_template("7-states_list.html", states=states.values())


if __name__ == "__main__":
    app.run()
