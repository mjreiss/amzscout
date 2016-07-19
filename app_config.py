import os
from app import app
from celery import Celery

IP = '127.0.0.1'
PORT = 5000
DEBUG = True
SECRET_KEY = 'abc123'
WTF_CSRF_SECRET_KEY = 'abc123'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
CSRF_ENABLED = True
USER_APP_NAME="Scout"
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']

# Local
# app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0' # `celery worker -A app.celery --loglevel=info`
# app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

# Production
app.config['CELERY_BROKER_URL'] = os.environ.get('CLOUDAMQP_URL')
app.config['CELERY_RESULT_BACKEND'] = os.environ.get('CLOUDAMQP_URL')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['AMZ_API_KEY'] = os.environ.get('AMZ_API_KEY')
app.config['AMZ_API_SECRET'] = os.environ.get('AMZ_API_SECRET')
app.config['AMZ_ASSOCIATE'] = os.environ.get('AMZ_ASSOCIATE')
app.config['MWS_API_KEY'] = os.environ.get('MWS_API_KEY')
app.config['MWS_API_SECRET'] = os.environ.get('MWS_API_SECRET')
app.config['MWS_TOKEN'] = os.environ.get('MWS_TOKEN')
app.config['MWS_SID'] = os.environ.get('MWS_SID')
app.config['AMZ_US'] = 'ATVPDKIKX0DER'
