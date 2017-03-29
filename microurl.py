import os
import random
import string
import sys
import time

from validators import url as urlcheck
from validators import domain as domaincheck
from validators import ipv4 as ipcheck
from flask import abort, Flask, g, redirect, render_template, request, url_for,\
                  send_from_directory

import database
import random_micro


#CONSTANTS#####################################################################
MICRO_LEN = 6   # The length of the shortened URL (micro URL).

LETTERS_DIGITS = string.ascii_letters + string.digits   # Letters to choose
                                                        # from when generating
                                                        # the micro URL.

#FLASK#########################################################################
app = Flask(__name__)   # Instantiate a flask app.

db = database.DB_Interface()


@app.route('/')
def route_index():
    '''
        Main index page handler.
    '''
    return render_template('index.html')


@app.route('/about')
def route_about():
    '''
        About page handler.
    '''
    return render_template('about.html')


@app.route('/all')
def route_all():
    '''
        All registered micros page handler.
    '''
    # Render the 'all' template with the url_registry (database of all micros).
    return render_template('all.html', registry=read_all())


@app.route('/generate_micro', methods=['POST'])
def route_generate_micro():
    '''
        Generate micro POST request handler.
    '''
    url = request.form['url']   # Get the 'url' value from the request.
    micro = generate_micro()    # Generate a random micro.
    register_micro(micro, url)  # Store the micro and URL in the database.

    return micro


@app.route('/<micro>')
def route_micro(micro):
    '''
        Micro to real URL redirection handler.
    '''
    try:
        temp = lookup_micro(micro)

        if urlcheck(temp):
            return redirect(temp)
        elif domaincheck(temp):
            return redirect("http://" + temp)
        elif ipcheck(temp.split(':')[0]) and urlcheck('http://' + temp):
            # checks for plain ip or an ip with something after it
            return redirect("http://" + temp)
        else:
            abort(404)
    except Exception as e:
        # If micro is not registered, handle the exception from trying to look
        # it up and raise a 404 HTTP error.
        sys.stderr.write(str(e))
        abort(404)


@app.errorhandler(404)
def route_404(error):
    '''
        Generate a 404 page.
    '''
    return 'invalid url'


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico')


#BUSINESS LOGIC################################################################
def generate_micro():
    '''
        Generates a random MICRO_LEN length ASCII code.
    '''
    return random_micro.random(3)


def lookup_micro(micro):
    '''
        Returns micro's associated url.
    '''
    try:
        return read_data(micro)
    except KeyError as e:
        raise e


def register_micro(micro, url):
    '''
        Stores a micro and URL pair in the database.
    '''
    DAY_SECS = 24 * 60 * 60

    with db:
        tnow = int(time.time())
        rc = db.insert(micro, url, tnow, tnow + DAY_SECS)


def read_all():
    '''
        Read all data from DB and return as dict.
    '''
    with db:
        data = db.get_all()

    if not(data):
        return {'': 'nothing here'}
    else:
        return {d[1] : d[2] for d in data}


def read_data(query):
    '''
        Search for and return a query in the DB otherwise raise Exception.
    '''
    with db:
        data = db.query(query)

    if not(data):
        raise KeyError('{} not found in database'.format(query))
    else:
        return data[2]
