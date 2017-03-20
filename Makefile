default:


run:
	#gunicorn -w 4 -b localhost:5000 -k gevent microURL:app
	FLASK_APP=microURL.py FLASK_DEBUG=1 flask run
