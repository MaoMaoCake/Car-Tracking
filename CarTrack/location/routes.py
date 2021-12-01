import os
from datetime import datetime
from CarTrack import db
from flask import Blueprint,request
from CarTrack.models import Location,Device


location = Blueprint('location', __name__)

@location.route('/api/add_location', methods=['POST'])
def add_location():
    if request.method == 'POST':
        try:
            device_id = request.args.get('device_id')
            dev_id = Device.query.filter_by(device_id=device_id).first()
            location = request.args.get('location')
            print(dev_id.id, location)
            location_obj = Location(device_id=dev_id.id, location=location, timestamp=datetime.now())
            db.session.add(location_obj)
            db.session.commit()
            return {'status': 'success'}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}
    return {'status': 'failed'}

@location.route('/api/get_location', methods=['GET'])
def get_location():
    if request.method == 'GET':
        device_id = request.args.get('device_id')
        locations = Location.query.filter_by(device_id=device_id).all()
        return {'status': 'success', 'locations': [location.location for location in locations]}
    return {'status': 'failed'}

@location.route('/api/map_key', methods=['GET'])
def get_map_key():
    if request.method == 'GET':
        return {'status': 'success', 'map_key': os.getenv('MAPBOX_KEY')}
    return {'status': 'failed'}