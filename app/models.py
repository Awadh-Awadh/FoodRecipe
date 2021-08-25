from .import db
from flask_login import UserMixin, login_manager

@login_manager.user_loaded
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())