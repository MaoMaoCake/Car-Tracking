import os

from CarTrack import db
from flask import Blueprint,request
from CarTrack.models import Location


location = Blueprint('location', __name__)

@location.route('/add_location', methods=['POST'])
def add_location():
    if request.method == 'POST':
        device_id = request.args.get('device_id')
        location = request.args.get('location')
        location_obj = Location(device_id=device_id, location=location)
        db.session.add(location_obj)
        db.session.commit()
        return {'status': 'success'}
    return {'status': 'failed'}

@location.route('/get_location', methods=['GET'])
def get_location():
    if request.method == 'GET':
        device_id = request.args.get('device_id')
        locations = Location.query.filter_by(device_id=device_id).all()
        return {'status': 'success', 'locations': [location.serialize() for location in locations]}
    return {'status': 'failed'}

@location.route('/api/map_key', methods=['GET'])
def get_map_key():
    if request.method == 'GET':
        return {'status': 'success', 'map_key': os.getenv('MAPBOX_KEY')}
    return {'status': 'failed'}