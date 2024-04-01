#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

python manage.py makemigrations
python manage.py migrate

./manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')"
