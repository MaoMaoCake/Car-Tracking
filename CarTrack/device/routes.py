from flask import Blueprint, render_template, request, redirect, url_for, flash

from CarTrack import db
from CarTrack.models import Device
from CarTrack.device.forms import AddTrackerForm

device = Blueprint('device', __name__)

@device.route('/add_device', methods=['POST'])
def add_device():
    form = AddTrackerForm()
    if form.validate_on_submit():
        device = Device(name=form.device_name.data,color=form.device_color.data,
                        password=form.device_password.data)
        db.session.add(device)
        db.session.commit()
        flash('Device added successfully!','success')
        return redirect(url_for('main.home'))
    return render_template('add_device.html', title="Add Device", form=form)