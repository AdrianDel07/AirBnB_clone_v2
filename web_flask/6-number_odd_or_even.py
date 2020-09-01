#!/usr/bin/python3
"""start flask python <number>"""

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """display Hello HBNB!"""
    return ('Hello HBNB!')


@app.route('/hbnb')
def hbnb():
    """display HBNB"""
    return ('HBNB')


@app.route('/c/<text>')
def c_isfun(text):
    """display C followed by value text"""
    return ('C {}'.format(text.replace("_", " ")))


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """display Python followed by value text"""
    return ('Python {}'.format(text.replace("_", " ")))


@app.route('/number/<int:n>')
def is_number(n):
    """display n is a number"""
    return ("{} is a number".format(n))


@app.route('/number_template/<int:n>')
def template_HTML(n):
    """display n in a Template HTML"""
    return (render_template('5-number.html', n=n))


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """display n if a odd or even"""
    return (render_template('6-number_odd_or_even.html', n=n))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
