from urllib.request import urlopen
from bs4 import BeautifulSoup
import redis
from bson import ObjectId
from bson.json_util import dumps, loads
from pymongo import MongoClient

from api import redis_port, redis_host
r = redis.StrictRedis(host=redis_host, port=redis_port, db=3)

db_name = 'e8'
def count_words(url = "http://kite.com", search_word="python"):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out

    # get text
    text = soup.get_text()

# class Message():
#     def __init__(self):
#         mongo_client = MongoClient('mongo')
#         collection = mongo_client[db_name]
#         self.db = collection.messages
#         self.result = False
#
#     def set(self, message):
#         try:
#             self.db.insert({'message': message})
#             self.result = True
#         except:
#             self.result = False
#
#     def get_all(self):
#         cursor = self.db.find()
#         messages = list(cursor)
#         return [item for item in messages]
#
#     def get(self, _id):
#         if r.exists(_id):
#             cursor = loads(r.get(_id))
#         else:
#             cursor = self.db.find({'_id': ObjectId(_id)})[0]
#             r.set(_id, dumps(cursor))
#         return cursor
#
#     def update_tags(self, _id, new_tag):
#         r.delete(_id)
#         self.db.update({'_id': ObjectId(_id)}, {'$push': {'tags': new_tag}})
#
#     def update_comments(self, _id, new_comment):
#         r.delete(_id)
#         self.db.update({'_id': ObjectId(_id)}, {'$push': {'comments': new_comment}})

