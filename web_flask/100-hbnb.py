#!/usr/bin/python3
""" module for Flask web application
"""
from flask import Flask
from flask import render_template

from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def states():
    """ script that starts a Flask web application:
    """

    states = sorted(storage.all(State).values(),
                    key=lambda state: state.name)

    amenities = sorted(storage.all(Amenity).values(),
                       key=lambda amenity: amenity.name)

    places = sorted(storage.all(Place).values(),
                    key=lambda place: place.name)

    return render_template("100-hbnb.html", states=states,
                           amenities=amenities, places=places)


@app.teardown_appcontext
def teardown_db(exception):
    """ remove the current SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
