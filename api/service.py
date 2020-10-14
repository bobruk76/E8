from _celery.tasks import count_words

from api import db
from api.models import Task

def new_url(url):
    new_task = Task(address=url)
    db.session.add(new_task)
    db.session.commit()
    count_words.delay(new_task.as_dict())





