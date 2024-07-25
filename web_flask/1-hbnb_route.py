#!/usr/bin/python3
"""
A module that demonstrates the flask routing
procedure
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """
    A function called when a user accesses the home
    page of our app
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_world():
    """
    A function called when a user accesses the hbnb
    page of our app
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
