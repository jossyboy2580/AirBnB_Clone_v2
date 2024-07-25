#!/usr/bin/python3
"""
A module that demonstrates the flask routing
procedure
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    A function called when a user accesses the home
    page of our app
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    A function called when a user accesses the hbnb
    page of our app
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """
    A function called when a user accesses the hbnb
    page of our app
    """
    text_list = list(text)
    for i in range(len(text_list)):
        if text_list[i] == '_':
            text_list[i] = ' '
    text = "".join(text_list)
    return f'C {text}'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
