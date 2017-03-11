[![Code Climate](https://codeclimate.com/github/francium/microURL/badges/gpa.svg)](https://codeclimate.com/github/francium/microURL)

Required
--------
Note some requirements in `requirements.txt` are for Heroku only. Below are the
actual requirements for running the application locally.

- Python 3 (Python 2 untested)
- Flask
- Requests

Use
---
Note these are \*nix instructions, usage on Windows may be different. Using a
\*nix system is *highly* recommended to avoid any undue frustration.

    $ export FLASK_APP=microURL.py
    $ flask run

This application has been successfully deployed to Heroku as well. The required
Heroku files are included,

- Procfile
- requirements.txt
- runtime.txt


See the [Flask documents](http://flask.pocoo.org/docs/0.12/) for more
information about using Flask.
