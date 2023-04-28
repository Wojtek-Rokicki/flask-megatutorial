from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users' # instead of default user
    id = db.Column(db.Integer, primary_key=True)
    google_id = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    verified_email = (db.Boolean)
    full_name = db.Column(db.String(128), index=True)
    given_name = db.Column(db.String(64))
    family_name = db.Column(db.String(64))
    picture_url = db.Column(db.String(128))
    localization = db.Column(db.String(8))
    posts = db.relationship('Post', backref='author', lazy='dynamic')


    def __repr__(self):
        return '<User {}>'.format(self.email)
    
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)