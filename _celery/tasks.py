from __future__ import absolute_import
from urllib.request import urlopen
from bs4 import BeautifulSoup
from _celery.celery import app

@app.task
def count_words(url="http://kite.com", search_word="python"):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out
    text = soup.get_text().lowcase()
    count = text.count(search_word)
    return count
