IP=127.0.0.1
PORT=5000


default:

debug:
	#gunicorn -w 4 -b localhost:5000 -k gevent microURL:app
	FLASK_APP=microURL.py FLASK_DEBUG=1 flask run

run:
	gunicorn -w 4 -b $(IP):$(PORT) -k gevent microURL:app
