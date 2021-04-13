FROM python:3.8

WORKDIR /apps/loco/

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD . .


EXPOSE 80