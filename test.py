from datetime import datetime
from secrets import token_urlsafe
from CarTrack import create_app, db, bcrypt
from CarTrack.models import Device, User, DeviceLink, Location

app = create_app()
app.app_context().push()
db.create_all()

# # create user
# password = bcrypt.generate_password_hash('maomao').decode('utf-8')
# maomao = User(username='maomao', email="maomao@m.m", password=password)
#
# # db.session.add(maomao)
# # db.session.commit()
#
# # create user
# password = bcrypt.generate_password_hash('asd').decode('utf-8')
# shield = User(username='shield', email="shield@s.s", password=password)
#
# db.session.add(shield)
# db.session.commit()
#
# get user
# maomao = User.query.filter_by(username='maomao').first()
# print(maomao)
#
# # make 1st device
# token = token_urlsafe(16)
# device = Device(name="MaoMao Tracker", color="red", device_id=token)
# db.session.add(device)
# db.session.commit()
#
# #make 2nd device
# token = token_urlsafe(16)
# device2 = Device(name="Shield Tracker", color="blue", device_id=token)
# db.session.add(device2)
# db.session.commit()
#
# # link devices
# link = DeviceLink(user_id=maomao.id, device_id=device.id,mode="owner")
# db.session.add(link)
# db.session.commit()
#
# #share device 1 to shield
# link2 = DeviceLink(user_id=shield.id, device_id=device.id,mode="guest")
# db.session.add(link2)
# db.session.commit()
#
# # make new device for shield
# link3 = DeviceLink(user_id=shield.id, device_id=device2.id,mode="owner")
# db.session.add(link3)
# db.session.commit()
#
# #share device 2 to maomao
# link4 = DeviceLink(user_id=maomao.id, device_id=device2.id,mode="guest")
# db.session.add(link4)
# db.session.commit()
#
# # make location
# loc_json = "{'lat': '1.1', 'lng': '2.2'}"
# loc = Location(device_id=device.id, location=loc_json,timestamp=datetime.now())
# db.session.add(loc)
# db.session.commit()

# print("MaoMao devices:", maomao.devices)
# print("Shield Devices:", shield.devices)
# print("Shield shared device:", DeviceLink.query.join(User).filter(User.id == shield.id).filter(DeviceLink.mode == "guest").first().device_id)
# print("Location Query:", Location.query.filter(Location.device_id == DeviceLink.query.join(User)\
#                                                .filter(User.id == shield.id)\
#                                                .filter(DeviceLink.mode == "guest").first().device_id).all()[0].timestamp)

maomao = User.query.filter_by(username='maomao').first()
device = Device.query.filter_by(id=2).first()
ids = DeviceLink.query.join(User).filter(User.id == maomao.id).filter(DeviceLink.mode == "owner").all()
for i in ids:
    print("Device name from User ID", Device.query.filter_by(id=i.device_id).first())
print("User ID from device:", DeviceLink.query.filter_by(device_id=device.id).filter_by(mode="owner").first().user_id)