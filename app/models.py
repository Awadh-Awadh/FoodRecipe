from .import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())