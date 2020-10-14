from __future__ import absolute_import
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup
from celery import Celery

# from _celery import nsq_host, nsq_port

app = Celery('first_celery')
app.config_from_object('config.ConfigCelery')

@app.task
def count_words(task_dict, search_word="python"):
    pass
    # class NSQD:
    #     def __init__(self, server=nsq_host, port=nsq_port):
    #         self.server = "http://{}:{}/pub".format(server, port)
    #
    #     def send(self, topic, msg):
    #         res = requests.post(self.server, params={"topic": topic}, data=msg)
    #         if res.ok:
    #             return res

    # new_nsqd = NSQD()
    # new_nsqd.send('tasks', search_word)

    # _urlopen = urlopen(task_dict.url)
    # task_dict.http_status = _urlopen.getcode()
    #
    # if task_dict.http_status <= 400:
    #     html = _urlopen.read()
    #     soup = BeautifulSoup(html, features="html.parser")
    #
    #     # kill all script and style elements
    #     for script in soup(["script", "style"]):
    #         script.extract()  # rip it out
    #     text = soup.get_text().lowcase()
    #     count = text.count(search_word)
    #
    # new_nsqd.send('tasks', task_dict)
    # print(msg=task_dict)

