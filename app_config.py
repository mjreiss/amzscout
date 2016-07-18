import os
from app import app
from celery import Celery

IP = '127.0.0.1'
PORT = 5000
DEBUG = True
SECRET_KEY = 'MAKE A KEY'
WTF_CSRF_SECRET_KEY = 'MAKE A KEY'
SQLALCHEMY_DATABASE_URI = 'sqlite:///scout.sqlite'
CSRF_ENABLED = True
USER_APP_NAME="AMZ Scout"
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']

app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0' # `celery worker -A app.celery --loglevel=info`
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['AMZ_API_KEY'] = 'YOUR PA API KEY'
app.config['AMZ_API_SECRET'] = 'YOUR PA API SECRET KEY'
app.config['AMZ_ASSOCIATE'] = 'YOUR ASSOCIATE KEY'
app.config['MWS_API_KEY'] = 'YOUR MWS KEY' #replace with your access key
app.config['MWS_API_SECRET'] = 'YOUR MWS SECRET KEY' #replace with your secret key
app.config['AMZ_US'] = 'ATVPDKIKX0DER'
app.config['MWS_TOKEN'] = ['YOUR TOKEN']
app.config['MWS_SID'] = ['YOUR SID']
