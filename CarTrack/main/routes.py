from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user
from CarTrack.models import User, DeviceLink, Device
main = Blueprint('main', __name__)

@main.route('/')
def home():
    if current_user.is_authenticated:
        my_device = []
        for i in DeviceLink.query.join(User).filter(User.id == current_user.id).filter(DeviceLink.mode == "owner").all():
            my_device.append(Device.query.filter_by(id=i.device_id).first())
        # query to find devices that are shared with the user
        shared_device = []
        for i in DeviceLink.query.join(User).filter(User.id == current_user.id).filter(DeviceLink.mode == "guest").all():
            shared_device.append(Device.query.filter_by(id=i.device_id).first())
        return render_template('home.html', title='Home', my_tracker=my_device, shared_tracker=shared_device)
    return render_template('home.html', title='Home')
