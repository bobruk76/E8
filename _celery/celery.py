from __future__ import absolute_import
from celery import Celery

app = Celery('test_celery',broker='redis://localhost', backend='redis://localhost',include=['_celery.tasks'])
