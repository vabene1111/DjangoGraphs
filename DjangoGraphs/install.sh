#!/usr/bin/env bash
docker-compose run web_graphs python3 manage.py createsuperuser
docker-compose run web_graphs python3 manage.py loaddata groups.json
