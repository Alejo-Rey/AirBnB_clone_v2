#!/usr/bin/python3
''' funtion using flask '''
from flask import Flask


app = Flask(__name__)
app.strict_slashes = False


@app.route('/')
def index():
    ''' send a index '''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    ''' routing path '''
    return 'HBNB'


@app.route('/c/<text>')
def c():
    ''' variable routing '''
    hi = 'C {}'.format(text.replace('_', ' '))
    return hi


@app.route('/python/')
@app.route('/python/<text>')
def py(text='is cool'):
    ''' pre cool '''
    hi = 'Python {}'.format(text.replace('_', ' '))
    return hi


@app.route('/number/<int:n>')
def num():
    ''' display only if is a numer '''
    return '%d is a number' % n


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
