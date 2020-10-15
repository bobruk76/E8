from _celery.tasks import count_words

from api import db
from api.models import Task, Result


def new_url(url):
    new_task = Task(address=url)
    db.session.add(new_task)
    new_result = Result(address=url)
    db.session.add(new_result)
    db.session.commit()
    count_words.delay(new_task.as_dict(), new_result.as_dict())





