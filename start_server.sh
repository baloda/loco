cd /apps/loco/

python -u manage.py makemigrations

python -u manage.py migrate

python -u manage.py loaddata datadump.json

gunicorn loco.wsgi:application --bind 0.0.0.0:80 --workers 3