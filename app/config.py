import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('POSTGRES_DATABASE_URL') or \
        'postgresql://users_admin:password@localhost/users' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False