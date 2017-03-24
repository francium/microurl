import os
import random
import string
import sys

from validators import url as urlcheck
from flask import abort, Flask, redirect, render_template, request, url_for,\
                  send_from_directory

import random_micro


#CONSTANTS#####################################################################
MICRO_LEN = 6   # The length of the shortened URL (micro URL).

LETTERS_DIGITS = string.ascii_letters + string.digits   # Letters to choose
                                                        # from when generating
                                                        # the micro URL.


#THE DATABASE##################################################################
DB = 'url_registry.txt' # It's not a real DB... for now.


#FLASK#########################################################################
app = Flask(__name__)   # Instantiate a flask app.


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
        temp = lookup_micro(micro).strip()

        if urlcheck(temp):
            return redirect(temp)
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
    write_data(micro + '=' + url)


def read_all():
    '''
        Read all data from DB and return as dict.
    '''
    all_data = {}
    try:
        with open(DB, 'r') as db:
            for ln in db:
                split_index = ln.find('=')
                all_data[ln[: split_index]] = ln[split_index + 1 :]
    except FileNotFoundError as fnfe:
        with open(DB, 'w'):
            pass

    return all_data if len(all_data) else {'': 'nothing here -'}


def read_data(query):
    '''
        Search for and return a query in the DB otherwise raise Exception.
    '''
    try:
        with open(DB, 'r') as db:
            for ln in db:
                if query in ln:
                    split_index = ln.find('=')
                    return ln[split_index + 1 :]
    except FileNotFoundError as fnfe:
        with open(DB, 'w'):
            pass

    raise KeyError('Query, "{}" not found.'.format(query))


def write_data(data):
    '''
        Append data to the DB
    '''
    with open(DB, 'a') as db:
        db.write(data + '\n')
