import enum
from datetime import datetime

from sqlalchemy import Enum, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

from api import db

Base = declarative_base()
metadata = Base.metadata

class Result(Base):
    __tablename__ = 'results'
    _id = Column(Integer, primary_key=True)
    address = Column(String(300), unique=False, nullable=True)
    words_count = Column(Integer, unique=False, nullable=True)
    http_status_code = Column(Integer)
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class TaskStatus (enum.Enum):
    NOT_STARTED = 1
    PENDING = 2
    FINISHED = 3

class Task(Base):
    __tablename__ = 'tasks'
    _id = Column(Integer, primary_key=True)
    address = Column(String(300), unique=False, nullable=True)
    timestamp = Column(DateTime(), default=datetime.utcnow)
    task_status = Column(Enum(TaskStatus))
    http_status = Column(Integer)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

