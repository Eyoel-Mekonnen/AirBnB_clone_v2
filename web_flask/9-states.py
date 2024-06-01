#!/usr/bin/python3
"""Start Application and retrieve State"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage

app = Flask(__name__)


@app.route("/states/", strict_slashes=False)
def states():
    all_states = storage.all("State")
    states = {}
    for key, value in all_states.items():
        states[key] = value
    state_id = None
    return render_template("9-states.html", states=states, state_id=state_id)

@app.route("/states/<id>", strict_slashes=False)
def states_with_id(id):
    all_states = storage.all("State")
    states = {}
    state_id = "Not found!"
    for key, state in all_states.items():
        if state.id == id:
            state_id = id
            states[key] = state
    return render_template("9-states.html", states=states, state_id=state_id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

