#!/usr/bin/env bash
docker-compose run web_graphs python3 manage.py migrate
docker-compose run web_graphs python3 manage.py collectstatic --noinput
