cd /apps/loco/

python -u manage.py makemigrations

python -u manage.py migrate

python -u manage.py loaddata datadump.json

# python -u manage.py collectstatic

gunicorn loco.wsgi:application --bind 0.0.0.0:8000 --workers 3