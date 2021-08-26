
class Recipe:
    def __init__(self,id,image,missedIngredients,unusedIngredients):
        self.id = id
        self.image = image
        self.missedIngredients = missedIngredients
        self.unusedIngredients = unusedIngredients
from .import db,login_manager
from flask_login import UserMixin




class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

