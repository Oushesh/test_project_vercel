#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Heroku collecstatic --noinput
python manage.py collectstatic --noinput

# Start Backend server
echo "Start server"
python manage.py runserver 0.0.0.0:8000

