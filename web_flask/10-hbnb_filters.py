#!/usr/bin/python3
"""HBNB filters Module"""

from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def hbnb():
    """display States, object found by id State and its cities"""
    all_states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return (render_template('10-hbnb_filters.html', **locals()))


@app.teardown_appcontext
def teardown(self):
    """function that call close methofd"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
