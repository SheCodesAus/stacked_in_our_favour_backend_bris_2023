rm -rf /dbvol/db.sqlite3
#!/usr/bin/env bash
python manage.py migrate
python manage.py createsuperuser --no-input
gunicorn --bind :8000 --workers 1 winstack.wsgi
