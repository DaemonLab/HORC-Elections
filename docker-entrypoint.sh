#!/usr/bin/bash

run_migrations() {
    python3 manage.py makemigrations &&
    python3 manage.py makemigrations voting &&
    python3 manage.py migrate --noinput;
}

create_superuser() {
    if [ "$DJANGO_SUPERUSER_PASSWORD" ];
    then
        python manage.py createsuperuser \
            --noinput \
            --username "${DJANGO_SUPERUSER_USERNAME:-admin}" \
            --email "${DJANGO_SUPERUSER_EMAIL:-admin@localhost}"
    fi
}

start_server(){
    exec gunicorn --bind 0.0.0.0:8000 horc_elections.wsgi
}

run_migrations && create_superuser && start_server;