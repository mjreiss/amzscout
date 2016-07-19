import os
from app import app
from celery import Celery

IP = '127.0.0.1'
PORT = 5000
DEBUG = True
SECRET_KEY = 'key'
WTF_CSRF_SECRET_KEY = 'secret_key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///scout.sqlite'
CSRF_ENABLED = True
USER_APP_NAME = 'Scout'
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']

app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0' # `celery worker -A app.celery --loglevel=info`
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['AMZ_API_KEY'] = 'AMZ_API_KEY' # AMZ PA API KEY
app.config['AMZ_API_SECRET'] = 'AMZ_API_SECRET' # AMZ PA API SECRET KEY
app.config['AMZ_ASSOCIATE'] = 'AMZ_ASSOCIATE' # AMZ ASSOCIATE TAG
app.config['MWS_API_KEY'] = 'MWS_API_KEY' # MWS API KEY
app.config['MWS_API_SECRET'] = 'MWS_API_SECRET' # MWS API SECRET KEY
app.config['AMZ_US'] = 'ATVPDKIKX0DER'

app.config['MWS_TOKEN'] = 'MWS_TOKEN' # AMZ MWS TOKEN

app.config['MWS_SID'] = 'MWS_SID' # AMZ SELLER ID
