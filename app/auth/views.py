from flask_login import login_manager
from . import auth
from flask import render_template,url_for,redirect,flash
from .forms import RegForm,LoginForm
from ..models import User
from app import bcrypt,db
from flask_login import login_user, logout_user,login_required,current_user




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




@auth.route('/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
      user = User.query.filter_by(email = form.email.data).first()
      if user and bcrypt.check_password_hash(user.password, form.password.data):
           login_user(user,remember = form.remember_me.data)
           flash("Login Successful",'success')
           return redirect('main.recipe')
      flash("Invalid userame or password",'danger')

  return render_template('login.html', form = form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()

    return render_template('hero.html')
