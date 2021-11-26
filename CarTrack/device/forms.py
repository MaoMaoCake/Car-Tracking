from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from CarTrack.models import Device

class AddTrackerForm(FlaskForm):
    device_name = StringField('Device Name', validators=[DataRequired(), Length(min=2, max=20)])
    device_color = StringField('Device Color', validators=[DataRequired(), Length(min=2, max=20)])
    device_id = StringField('Device ID', validators=[DataRequired(), Length(min=2, max=20)])
    device_password = PasswordField('Device Password', validators=[DataRequired(), Length(min=2, max=20)])
    confirm_device_password = PasswordField('Confirm Device Password', validators=[DataRequired(),
                                                                                   Length(min=2, max=20),
                                                                                   EqualTo('device_password')])
    submit = SubmitField('Add Device')

    def validate_device_id(self, device_id):
        device = Device.query.filter_by(device_id=device_id.data).first()
        if device:
            raise ValidationError('This device is already registered.')