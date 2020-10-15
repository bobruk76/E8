import os
import json
from json import JSONDecodeError
from marshmallow import Schema, fields, pprint
import nsq

from api import db
from api.models import Result


class ResultSchema(Schema):
    _id = fields.Integer()
    address = fields.Str()
    words_count = fields.Integer()
    http_status_code = fields.Integer()

TCP_ADDRESSES = [os.getenv('TCP_ADDRESSES', 'http://localhost:4150')]

TASKS = {}
RESULTS = {}

def occurance(value, value_type):
    if value in value_type.keys():
        value_type[value] += 1
    value_type[value] = 1

def handler_result(message):
    schema = ResultSchema()
    try:

        results = schema.loads(message.body.decode())
        for item in results:
            _id = item["_id"]
            result = Result.query.get_or_404(_id)
            if result:
                result.words_count = int(item["words_count"])
                result.words_count = int(item["words_count"])
                db.session.add(result)

        db.session.commit()
        return True
    except JSONDecodeError:
        return False

r = nsq.Reader(message_handler=handler_result,
        nsqd_tcp_addresses=TCP_ADDRESSES,
        topic='results',
        channel='consumer_channel', lookupd_poll_interval=15)

if __name__ == '__main__':
    nsq.run()
