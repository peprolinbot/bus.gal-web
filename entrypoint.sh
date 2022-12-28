#!/bin/sh

gunicorn busGal_Django.wsgi -b 0.0.0.0:8000 --timeout 0 &

nginx -g 'daemon off;'
