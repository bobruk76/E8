import os


from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

redis_host = str(os.environ.get("REDIS_HOST", "localhost"))
redis_port = int(os.environ.get("REDIS_PORT", 6379))

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from api import routes