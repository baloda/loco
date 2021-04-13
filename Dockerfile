FROM python:3.8

ADD requirements.py .

RUN pip install requirements.py

ADD . .
