FROM python:3.8-alpine

RUN apk add --no-cache --virtual .build-deps gcc postgresql-dev musl-dev python3-dev
RUN apk add libpq

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

RUN apk del --no-cache .build-deps

RUN mkdir -p /code
COPY *.py /code/
WORKDIR /code
ENV SET FLASK_APP=flask_app.py FLASK_DEBUG=1 PYTHONUNBUFFERED=1
CMD flask run --host=127.0.0.1 --port=5000
