#!/usr/bin/python3
"""
A module that demonstrates the flask routing
procedure
"""
from flask import Flask
from flask import render_template


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


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def python_text(text='is cool'):
    """
    A function called when a user accesses the hbnb
    page of our app
    """
    text_list = list(text)
    for i in range(len(text_list)):
        if text_list[i] == '_':
            text_list[i] = ' '
    text = "".join(text_list)
    return f'Python {text}'


@app.route("/number/<int:number>", strict_slashes=False)
def number_route(number):
    """
    A function for printing a routed number
    """
    return f'{number} is a number'


@app.route("/number_template/<int:number>", strict_slashes=False)
def number_template_route(number):
    """
    A function for printing a routed number template
    """
    return render_template('5-number.html', number=number)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
