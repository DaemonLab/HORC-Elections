#!/usr/bin/bash

python3 manage.py makemigrations &&
python3 manage.py migrate --noinput;

if [ "$DJANGO_SUPERUSER_PASSWORD" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username "${DJANGO_SUPERUSER_USERNAME:-admin}" \
        --email "${DJANGO_SUPERUSER_EMAIL:-admin@localhost}"
fi

gunicorn --bind 0.0.0.0:8000 horc_elections.wsgi



python manage.py createsuperuser \
    --noinput \
    --username "${DJANGO_SUPERUSER_USERNAME}" \
    --email "${DJANGO_SUPERUSER_EMAIL}"