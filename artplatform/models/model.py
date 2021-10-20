from ..database import database as db
from datetime import datetime
from flask_login import UserMixin


class UserLogin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String(30), unique=True, nullable=False)
    # password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    posts = db.relationship('Post', backref='author', lazy='dynamic')


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    image_url = db.Column(db.String, nullable=False)
    video_url = db.Column(db.String) # add video 
    audio_url = db.Column(db.String) # add audio
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user_login.id'))
