from flask import Blueprint, render_template, request, redirect, url_for, flash
from CarTrack.models import User
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html',title='Home',my_tracker=["My Tracker 1","My Tracker 2","My Tracker 3"],
                           shared_tracker=["Shared Tracker 1","Shared Tracker 2","Shared Tracker 3"])
