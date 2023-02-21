#!/bin/sh

>&2 echo "Database is up - executing command"
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000