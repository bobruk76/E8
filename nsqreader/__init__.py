import os

nsq_host = str(os.environ.get("NSQ_HOST", "localhost"))
nsq_port = int(os.environ.get("NSQ_PORT", 4150))

db_uri = str(os.environ.get("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/e8"))

