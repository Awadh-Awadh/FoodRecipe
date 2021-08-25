from . import auth
from flask import render_template,url_for,redirect,flash


@auth.route('/register')
def register():


    return render_template('auth/register.html')
