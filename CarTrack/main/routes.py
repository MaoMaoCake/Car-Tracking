from flask import Blueprint, render_template, request, redirect, url_for, flash

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')
