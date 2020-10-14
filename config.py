import os

class Config:
    FLASK_APP = "app.py"
    FLASK_DEBUG = 1
    FLASK_ENV = 'development'

    SECRET_KEY = os.urandom(32)
    PORT = os.getenv('PORT', 5000)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ConfigCelery:
    result_expires = 3600
    broker = 'redis://localhost'
    # result_backend = 'redis://localhost'
    include = ['_celery.tasks']
