from flask import Flask
from app.config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# There are serveral ways to configure your app:
# app.config['SECRET_KEY'] = 'you-will-never-guess'
# The other one, which is more separation of concerns alike:
# In config.py: Secret key configuration
# import os
# class Config(object):
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
# The Flask-WTF extension uses SECRET_KEY to protect web forms against a nasty attack called Cross-Site Request Forgery
# The other use of this variable is for cryptographic purposes

from app import routes, models