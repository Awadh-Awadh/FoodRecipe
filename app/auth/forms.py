from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Length,DataRequired,Email,EqualTo,ValidationError
from ..models import User



class RegForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    email = StringField('Enter your email',validators=[DataRequired(), Email()])
    password = PasswordField('password',validators=[DataRequired(),Length(min=6),EqualTo('confirm_password', message = 'passwords must match')])
    confirm_password = PasswordField('Confirm password',validators=[DataRequired()])
    submit = SubmitField('Register')



    def validate_username(self,username):
        username = User.query.filter_by(username = username.data).first()
        if username:
            raise ValidationError("Username already exist. Please use another username")

    def validate_email(self,email):
        email = User.query.filter_by(email = email.data).first()
        if email:
            raise ValidationError("Email already exist. Please use another username")



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
    Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')