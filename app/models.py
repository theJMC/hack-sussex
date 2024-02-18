from sqlalchemy import ForeignKey

from app import db


class User(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    token = db.Column(db.String(1000))
    overall_status = db.Column(db.Integer)


class Plant(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100))
    type = db.Column(db.String(100))
    sunlight = db.Column(db.Integer)
    water = db.Column(db.Integer)
    notes = db.Column(db.String(300))
    vibes = db.Column(db.String(100))
    species = db.Column(db.String(100))
    owner = db.Column(db.String(100), ForeignKey('user.id'))
    muted = db.Column(db.Boolean)
