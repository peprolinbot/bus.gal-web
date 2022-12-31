#!/bin/sh

gunicorn busGal_Django.wsgi -b 0.0.0.0:8000 --workers $GUNICORN_WORKERS --timeout $GUNICORN_TIMEOUT &

nginx -g 'daemon off;'
