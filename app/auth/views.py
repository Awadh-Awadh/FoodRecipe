from flask_login import login_manager
from . import auth
from flask import render_template,url_for,redirect,flash
from .forms import RegForm
from ..models import User
from app import bcrypt,db




@auth.route('/register', methods = ['GET','POST'])
def register():
    form = RegForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data,password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Account creation successfull. You can now login",'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html', form = form)




@auth.route('/login')
def login():

  return render_template('auth/login.html')