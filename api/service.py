from _celery.tasks import count_words

# from api import redis_port, redis_host
# r = redis.StrictRedis(host=redis_host, port=redis_port, db=3)

import requests

from api import db
from api.models import Task

def new_url(url):
    new_task = Task(address=url)
    db.session.add(new_task)
    db.session.commit()
    count_words.delay(new_task.as_dict())
    print(new_task.as_dict())




