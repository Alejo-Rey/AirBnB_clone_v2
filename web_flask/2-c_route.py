#!/usr/bin/python3
''' Using Flask variables '''
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    ''' say hello in index '''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    ''' say hello routing '''
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    ''' print variable '''
    hi = 'C {}'.format(text.replace('_', ' '))
    return hi

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
