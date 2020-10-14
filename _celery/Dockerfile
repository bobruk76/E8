FROM python:2.7

COPY _celery/requirements.txt /opt/pip/requirements.txt
RUN pip install -r /opt/pip/requirements.txt

ADD . /app/
WORKDIR /app/

ENTRYPOINT celery -A _celery worker --concurrency=20 --loglevel=DEBUG
