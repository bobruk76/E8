from __future__ import absolute_import
# from urllib.request import urlopen
import json
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup


from _celery import nsq_host, nsq_port
from _celery.celery import app


@app.task
def count_words(task_dict, result_dict, search_word="python"):
    class NSQD:
        def __init__(self, server=nsq_host, port=nsq_port):
            self.server = "http://{}:{}/pub".format(server, port)

        def send(self, topic, msg):
            res = requests.post(self.server, params={"topic": topic}, data=msg)
            if res.ok:
                return res

    new_nsqd = NSQD()

    _urlopen = urlopen(task_dict['address'])
    task_dict['http_status'] = _urlopen.getcode()
    result_dict['http_status_code'] = task_dict['http_status']

    if task_dict['http_status'] <= 400:
        html = _urlopen.read()
        soup = BeautifulSoup(html, features="html.parser")

        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()  # rip it out
        text = soup.get_text().lower()
        result_dict['words_count'] = text.count(search_word)
        new_nsqd.send('results', json.dumps(result_dict))

    new_nsqd.send('tasks', json.dumps(task_dict))


