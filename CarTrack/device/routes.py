from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from CarTrack import db
from CarTrack.models import Device
from CarTrack.device.forms import AddTrackerForm
from CarTrack.models import User, DeviceLink

device = Blueprint('device', __name__)

@device.route('/add_device', methods=['POST', 'GET'])
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

@device.route('/settings/<int:user_id>', methods=['GET', 'POST'])
@login_required
def settings(user_id):
    if user_id != current_user.id:
        flash('You cannot edit other users settings!','danger')
        return redirect(url_for('main.home'))
    user = User.query.get_or_404(user_id)
    # queries are used to get the device objects of the user and bind them to the link
    # query to find devices that are belong to the user
    my_device = []
    for i in DeviceLink.query.join(User).filter(User.id == user.id).filter(DeviceLink.mode == "owner").all():
        my_device.append(Device.query.filter_by(id=i.device_id).first())
    # query to find devices that are shared with the user
    shared_device = []
    for i in DeviceLink.query.join(User).filter(User.id == user.id).filter(DeviceLink.mode == "guest").all():
        shared_device.append(Device.query.filter_by(id=i.device_id).first())
    print(my_device)
    print(shared_device)
    return render_template('device_settings.html', title="Device Settings", my_device=my_device, shared_device=shared_device)

@device.route('/manage_device/<int:device_id>', methods=['GET', 'POST'])
@login_required
def manage_devices(device_id):
    device = Device.query.get_or_404(device_id)
    owner_id = DeviceLink.query.filter_by(device_id=device.id).filter_by(mode="owner").first().user_id
    if owner_id != current_user.id:
        flash('You cannot manage other users devices!','danger')
        return redirect(url_for('main.home'))
    return render_template('manage_device.html', title="Manage Device", device=device)