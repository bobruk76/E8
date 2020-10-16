import os
import json
import nsq

from marshmallow import Schema, fields, pprint
from sqlalchemy import update, table, column, create_engine
from nsqreader import db_uri, nsq_host, nsq_port
# import os
#
# nsq_host = str(os.environ.get("NSQ_HOST", "localhost"))
# nsq_port = int(os.environ.get("NSQ_PORT", 4150))

# db_uri = str(os.environ.get("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/e8"))
from nsqreader import db_uri

db_engine = create_engine(db_uri)


def handler_task(message):

    class TaskSchema(Schema):
        _id = fields.Integer()
        address = fields.Str()
        timestamp = fields.Str()
        task_stat = fields.Integer()
        http_status = fields.Integer()

    schema = TaskSchema()
    db_tasks = table("tasks",
                       column("_id"),
                       column("address"),
                       column("timestamp"),
                       column("task_stat"),
                       column("http_status"),
                       )

    try:

        item = schema.loads(message.body.decode())

        print(item)
        _id = int(item['_id'])

        stmt = update(db_tasks).where(db_tasks.c._id == _id). \
            values(http_status=int(item["http_status"]),)

        db_engine.execute(stmt)

        return True
    except:
        return False


def handler_result(message):

    class ResultSchema(Schema):
        _id = fields.Integer()
        address = fields.Str()
        words_count = fields.Integer()
        http_status_code = fields.Integer()

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

t = nsq.Reader(message_handler=handler_task,
               nsqd_tcp_addresses=['{}:{}'.format(nsq_host, nsq_port)],
               topic='tasks',
               channel='nsqreader_channel_tasks',
               lookupd_poll_interval=15)


if __name__ == '__main__':
    nsq.run()
