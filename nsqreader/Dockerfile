FROM python:3.8.5

COPY nsqreader/requirements.txt /opt/pip/requirements.txt
RUN pip install -r /opt/pip/requirements.txt

ADD . /app
WORKDIR /app
COPY ./* /app/

ENTRYPOINT ["python"]
CMD ["app.py"]
