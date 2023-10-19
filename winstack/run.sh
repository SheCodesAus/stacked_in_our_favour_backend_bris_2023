#!/usr/bin/env bash
rm -rf /dbvol/db.sqlite3
python manage.py migrate
python manage.py createsuperuser --no-input
gunicorn --bind :8000 --workers 1 winstack.wsgi
