#!/bin/bash
cd /home/ec2-user/django-app
source venv/bin/activate
gunicorn myproject.wsgi:application --bind 0.0.0.0:8000 --daemon
