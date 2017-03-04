from flask import abort, Flask, redirect, render_template, request, url_for

import random
import string


#CONSTANTS#####################################################################
MICRO_LEN = 6   # The length of the shortened URL (micro URL).

LETTERS_DIGITS = string.ascii_letters + string.digits   # Letters to choose
                                                        # from when generating
                                                        # the micro URL.


#THE DATABASE##################################################################
url_registry = {}   # It's for demonstration purposes only.
                    # It's not really a database, but it does the same thing.


#FLASK#########################################################################
app = Flask(__name__)   # Instantiate a flask app.


@app.route('/')
def route_index():
    '''
        Main index page handler.
    '''
    return render_template('index.html')


@app.route('/all')
def route_all():
    '''
        All registered micros page handler.
    '''
    # Render the 'all' template with the url_registry (database of all micros).
    return render_template('all.html', registry=url_registry)


@app.route('/generate_micro', methods=['POST'])
def route_generate_micro():
    '''
        Generate micro POST request handler.
    '''
    url = request.form['url']   # Get the 'url' value from the request.
    micro = generate_micro()    # Generate a random micro.
    register_micro(micro, url)  # Store the micro and URL in the database.

    # Render micro template with the micro and full URL of the micro.
    # FIXME Hardcoded server name.
    return render_template('micro.html', micro=micro,
          full_micro_url='localhost:5000/{}'.format(micro))


@app.route('/<micro>')
def route_micro(micro):
    '''
        Micro to real URL redirection handler.
    '''
    try:
        # If micro is registered, redirect to the associated URL.
        return redirect('http://' + lookup_micro(micro))
    except:
        # If micro is not registered, handle the exception from trying to look
        # it up and raise a 404 HTTP error.
        abort(404)


@app.errorhandler(404)
def route_404(error):
    '''
        Generate a 404 page.
    '''
    return 'invalid url'


#BUSINESS LOGIC################################################################
def generate_micro():
    '''
        Generates a random MICRO_LEN length ASCII code.
    '''
    return ''.join(random.choices(LETTERS_DIGITS, k=MICRO_LEN))


def lookup_micro(micro):
    '''
        Returns micro's associated url.
    '''
    return url_registry[micro]


def register_micro(micro, url):
    '''
        Stores a micro and URL pair in the database.
    '''
    url_registry[micro] = url
