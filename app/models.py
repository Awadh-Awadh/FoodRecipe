from .import db


class Users(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())