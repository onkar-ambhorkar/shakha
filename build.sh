#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

./manage.py makemigrations
./manage.py migrate

./manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')"
