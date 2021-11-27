from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from flask_login import login_required, current_user, login_user, logout_user

from CarTrack import db, bcrypt
from CarTrack.models import User
from CarTrack.users.forms import RegistrationForm, LoginForm, EditProfileForm
from CarTrack.users.utils import save_picture

users = Blueprint('users', __name__)

@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html',title='Login',form=form)

@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html',title='Register',form=form)

@users.route('/profile/<int:id>',methods=['GET','POST'])
@login_required
def profile(id):
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    if id == current_user.id:
        # if the user is viewing their own profile render form
        form = EditProfileForm()
        if form.validate_on_submit():
            if form.picture.data:
                picture_file = save_picture(form.picture.data)
                current_user.image_file = picture_file
            current_user.username = form.username.data
            current_user.email = form.email.data
            current_user.password = form.new_password.data
            db.session.commit()
            flash('Your changes have been saved.', 'success')
            print("changed_password")
            return redirect(url_for('users.profile', id=current_user.id))
        elif request.method == "GET":
            form.username.data = current_user.username
            form.email.data = current_user.email
            return render_template('profile.html', title='Profile', form=form,user=current_user, image_file=image_file)
    else:
        # if the user is not viewing their own profile render the profile page
        user = User.query.get_or_404(id)
        return render_template('profile.html',title='Profile', image_file=image_file, user=user)

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))