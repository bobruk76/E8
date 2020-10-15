import os
import json
import nsq

from marshmallow import Schema, fields, pprint
from sqlalchemy import update, table, column, create_engine
# from nsqreader import db_uri, nsq_host, nsq_port
import os

nsq_host = str(os.environ.get("NSQ_HOST", "localhost"))
nsq_port = int(os.environ.get("NSQ_PORT", 4150))

db_uri = str(os.environ.get("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/e8"))
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
        item = schema.loads(message.body.decode())

        print(item)
        _id = int(item['_id'])

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
