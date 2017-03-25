IP=127.0.0.1
PORT=5000

IP_DPLY=0.0.0.0
PORT_DPLY=80


default:

init:
	pip install -r requirements.txt

debug:
	FLASK_APP=microurl.py FLASK_DEBUG=1 flask run

run:
	gunicorn -w 4 -b $(IP):$(PORT) -k gevent microurl:app


dply_debug:
	echo ===WARNING: USE WITH EXTREME CARE===
	FLASK_APP=microurl.py FLASK_DEBUG=1 flask run --host $(IP_DPLY)\
		--port $(PORT_DPLY)

dply_run:
	gunicorn -w 4 -b $(IP_DPLY):$(PORT_DPLY) -k gevent microurl:app
