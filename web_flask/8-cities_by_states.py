#!/usr/bin/python3
"""Start a Flask application and retrieve city and state"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage

app = Flask(__name__)

@app.route("/cities_by_states", strict_slashes=False)
def city_by_state():
    all_states = storage.all("State")
    states = {}
    for key, value in all_states.items():
        states[key] = value
    return render_template("8-cities_by_states.html", states=states)

@app.teardown_appcontext
def tear_down(exec):
    storage.close()

if __name__== "__main__":
    app.run(host="0.0.0.0")
