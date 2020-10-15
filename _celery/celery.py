from __future__ import absolute_import
from celery import Celery

from _celery import broker_host

app = Celery('_celery', broker=broker_host, backend=broker_host, include=['_celery.tasks'])
