#!/bin/bash

NAME="gunicorn"
ROOTDIR=/demoproject/demosite/

NUM_WORKERS=1

cd $ROOTDIR

DJANGO_WSGI_MODULE=demosite.wsgi

exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --bind=0.0.0.0:80 \
  --log-level=info \
  --access-logfile=- \
  --timeout=20 \
  --reload
