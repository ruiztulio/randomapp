#!/bin/bash
export DJANGO_SETTINGS_MODULE=randomapp.settings

exec gunicorn randomapp.wsgi:application \
    --name randomapp_main \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --log-level=info
