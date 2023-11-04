#!/bin/sh

python manage.py migrate --run-syncdb

gunicorn busGal_Django.wsgi --preload -b 0.0.0.0:8000 --workers ${GUNICORN_WORKERS:-3} --timeout ${GUNICORN_TIMEOUT:-30} &
python3 manage.py qcluster &

nginx -g 'daemon off;'
