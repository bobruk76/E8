FROM python:3.8.5

COPY _celery/requirements.txt /opt/pip/requirements.txt
RUN pip install -r /opt/pip/requirements.txt

ADD . /app
WORKDIR /app

CMD python app/consumer.py