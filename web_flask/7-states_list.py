#!/usr/bin/python3
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def states():
    from models import storage
    from models.state import State
    states = storage.all("State")
    print(states)
    return (render_template("7-states_list.html", states=states))
    
@app.teardown_appcontext
def close_connection(error):
    from models import storage
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
