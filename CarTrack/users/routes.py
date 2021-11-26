from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user, login_user, logout_user

from CarTrack import db, bcrypt
from CarTrack.models import User

users = Blueprint('users', __name__)

@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    # login here
    return render_template('login.html',title='Login')

@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    # register here
    return render_template('register.html')

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))