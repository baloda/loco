cd /apps/loco/

python -u manage.py makemigrations

python -u manage.py migrate

gunicorn loco.wsgi:application --bind 0.0.0.0:80 --workers 3