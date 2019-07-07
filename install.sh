#!/usr/bin/env bash
docker-compose run web_graphs python3 manage.py migrate
docker-compose run web_graphs python3 manage.py collectstatic --noinput
docker-compose run web_graphs python3 manage.py createsuperuser
docker-compose run web_graphs python3 manage.py loaddata groups.json
docker-compose run web_graphs python3 manage.py loaddata settings.json