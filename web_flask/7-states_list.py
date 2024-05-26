#!/usr/bin/python3
"""Fetches from db and renders"""

from flask import Flask, render_template
from markupsafe import escape
from models import storage


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states():
    all_states = storage.all(State)
    states = {}
    for key, value in all_states.items():
        if key is not None and getattr(value, 'name', None) is not None:
            states[key] = value
    return (render_template("7-states_list.html", states=states))


@app.teardown_appcontext
def close_connection(exc):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
