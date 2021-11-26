from CarTrack import db, login_manager
from flask_login import UserMixin
from flask import current_app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

device_owner_identifier = db.Table('device_owner_identifier',
    db.Column('device_id', db.Integer, db.ForeignKey('device.id')),
    db.Column('owner_id', db.Integer, db.ForeignKey('user.id')),
    # mode is either 'owner' or 'guest' this shows affects how the device is displayed in the user's device list
    db.Column('mode', db.String(5))
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    devices = db.relationship('Device', secondary=device_owner_identifier)

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    color = db.Column(db.String(20), nullable=False)
    # optional password to protect the device from being added by other users
    password = db.Column(db.String(60), nullable=True)
    locations = db.relationship('Location',backref='device', lazy=True)

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(40), nullable=False)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))
