from flask import Flask
from flask_mail import Mail, Message
from celery import Celery
from flask_sqlalchemy import SQLAlchemy

# setup app
app = Flask(__name__)
app.config.from_object('config')

app.config['UPLOAD_FOLDER'] = 'app/files/uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['csv'])

# setup database
db = SQLAlchemy(app)

# Initialize Flask extensions
app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_DEFAULT_SENDER='"MyApp" <noreply@example.com>',
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'mjreiss4@gmail.com',
	MAIL_PASSWORD = '-'
	)

def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

mail=Mail(app)
celery = make_celery(app)

from app import views