from flask import Flask
from app import app, db

# from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter

class Scouts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.String, unique=True)
    filename = db.Column(db.String, unique=True)
    result = db.Column(db.String, unique=True)
    error = db.Column(db.String, unique=True)
    status = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    def __init__(self, task_id, filename, result, error, status):
        self.task_id = task_id
        self.filename = filename
        self.result = result
        self.error = error
        self.status = status

# class User(db.Model, UserMixin):
# 	id = db.Column(db.Integer, primary_key=True)

# 	# User authentication information
# 	username = db.Column(db.String(50), nullable=False, unique=True)
# 	password = db.Column(db.String(255), nullable=False, server_default='')
# 	reset_password_token = db.Column(db.String(100), nullable=False, server_default='')

# 	# User email information
# 	email = db.Column(db.String(255), nullable=False, unique=True)
# 	confirmed_at = db.Column(db.DateTime())

# 	# User information
# 	active = db.Column('is_active', db.Boolean(), nullable=False, server_default='0')
# 	first_name = db.Column(db.String(100), nullable=False, server_default='')
# 	last_name = db.Column(db.String(100), nullable=False, server_default='')


# # Setup Flask-User
# db_adapter = SQLAlchemyAdapter(db, User) # Register the User model
# user_manager = UserManager(db_adapter, app) # Initialize Flask-User