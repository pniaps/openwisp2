#!/bin/bash
docker-compose up -d redis influxdb
celery -A openwisp2 worker -l info &
celery -A openwisp2 beat -l info &
python manage.py runserver 0.0.0.0:8000
