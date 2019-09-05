#!/usr/bin/python3
''' import Flask '''
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def display_states():
    ''' display states '''
    all_states = storage.all("State")
    return render_template('7-states_list.html', State=all_states)


@app.route('/cities_by_states')
def display_states_cities():
    ''' display states with its cities '''
    all_states = storage.all("State")
    all_cities = storage.all("City")
    return render_template('8-cities_by_states.html',
                           State=all_states, City=all_cities)


@app.route('/states')
@app.route('/states/<id>')
def state_id(id=None):
    ''' display states with its cities '''
    all_states = storage.all("State")
    all_cities = storage.all("City")
    return render_template('9-states.html',
                           State=all_states, City=all_cities, id=id)


@app.teardown_appcontext
def close_method(exception=None):
    ''' close ssesions '''
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
