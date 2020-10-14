from urllib.request import urlopen
from bs4 import BeautifulSoup

# from api import redis_port, redis_host
# r = redis.StrictRedis(host=redis_host, port=redis_port, db=3)

import requests

from api import db, nsq_host, nsq_port
from api.models import Task

class NSQD:
    def __init__(self, server=nsq_host, port=nsq_port):
        self.server = "http://{}:{}/pub".format(server, port)

    def send(self, topic, msg):
        res = requests.post(self.server, params={"topic": topic}, data=msg)
        if res.ok:
            return res

def new_url(url):
    new_task = Task(address=url)
    db.session.add(new_task)
    db.session.commit()


