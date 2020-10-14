from urllib.request import urlopen
from bs4 import BeautifulSoup
import redis
from bson import ObjectId
from bson.json_util import dumps, loads
from pymongo import MongoClient
#
# from api import redis_port, redis_host
# r = redis.StrictRedis(host=redis_host, port=redis_port, db=3)

import requests

from api import db
from api.models import Task


class NSQD:
    def __init__(self, server='127.0.0.1', port=4151):
        self.server = "http://{}:{}/pub".format(server, port)

    def send(self, topic, msg):
        res = requests.post(self.server, params={"topic": topic}, data=msg)
        if res.ok:
            return res

def new_url(url):
    new_task = Task(url=url)
    db.session.add(new_task)
    db.session.commit()


def count_words(url = "http://kite.com", search_word = "python"):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out
