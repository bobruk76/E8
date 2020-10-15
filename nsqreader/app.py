import os
import json
import nsq

from marshmallow import Schema, fields, pprint
from sqlalchemy import update, table, column, create_engine
from nsqreader import db_uri, nsq_host, nsq_port

class ResultSchema(Schema):
    _id = fields.Integer()
    address = fields.Str()
    words_count = fields.Integer()
    http_status_code = fields.Integer()

TASKS = {}
RESULTS = {}

def handler_result(message):
    schema = ResultSchema()
    db_results = table("results",
                       column("_id"),
                       column("address"),
                       column("words_count"),
                       column("http_status_code"),
                       )
    try:
        db_engine = create_engine(db_uri)
        results = schema.loads(message.body.decode())
        for item in results:
            _id = int(item["_id"])

            stmt = update(db_results).where(db_results.c._id == _id). \
                values(words_count=int(item["words_count"]),
                       http_status_code=int(item["http_status_code"]))

            db_engine.execute(stmt)

        return True
    except:
        return False

r = nsq.Reader(message_handler=handler_result,
               nsqd_tcp_addresses=['{}:{}'.format(nsq_host, nsq_port)],
               topic='results',
               channel='nsqreader_channel',
               lookupd_poll_interval=15)

if __name__ == '__main__':
    nsq.run()
