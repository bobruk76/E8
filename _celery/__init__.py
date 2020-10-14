import os

nsq_host = str(os.environ.get("NSQ_HOST", "localhost"))
nsq_port = int(os.environ.get("NSQ_PORT", 4151))
