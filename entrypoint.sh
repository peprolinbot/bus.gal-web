#!/bin/sh

python manage.py migrate

gunicorn busGal_Django.wsgi --preload -b 0.0.0.0:8000 --workers ${GUNICORN_WORKERS:-3} --timeout ${GUNICORN_TIMEOUT:-30} &

nginx -g 'daemon off;'
