from __future__ import absolute_import
from celery import Celery

app = Celery('_celery', broker='redis://localhost:6379/8', backend='redis://localhost:6379/8', include=['_celery.tasks'])
