#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuserwithpassword --username admin --password admin --email admin@example.org --preserve
