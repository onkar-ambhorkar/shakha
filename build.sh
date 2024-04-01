#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate

if [[-z $CREATE_SUPERUSER]];
then
  python manage.py createsuperuser
fi
