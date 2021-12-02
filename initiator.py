from datetime import datetime
from secrets import token_urlsafe
from CarTrack import create_app, db, bcrypt
from CarTrack.models import Device, User, DeviceLink, Location

# create the app
app = create_app()
# push the db context
app.app_context().push()
print("creating app tables")
# create all the tables
db.create_all()

print("creating default users")
# create user called maomao with password maomao
password = bcrypt.generate_password_hash('maomao').decode('utf-8')
maomao = User(username='maomao', email="maomao@m.m", password=password)

# add the user and commit to the db
db.session.add(maomao)
db.session.commit()

# create user callled shield with password shield
password = bcrypt.generate_password_hash('shield').decode('utf-8')
shield = User(username='shield', email="shield@s.s", password=password)

# add the user and commit to the db
db.session.add(shield)
db.session.commit()

# create user called ohm with password ohm
password = bcrypt.generate_password_hash('ohm').decode('utf-8')
ohm = User(username='ohm', email="ohm@o.o", password=password)

# add the user and commit to the db
db.session.add(ohm)
db.session.commit()

# get user with username maomao
maomao = User.query.filter_by(username='maomao').first()
print(maomao)

## Create a device called Maomao Tracker
# make 1st device
print("creating devices")
token = token_urlsafe(16)
device = Device(name="MaoMao Tracker", color="red", device_id=token)
db.session.add(device)
db.session.commit()

#make 2nd device
token = token_urlsafe(16)
device2 = Device(name="Shield Tracker", color="blue", device_id=token)
db.session.add(device2)
db.session.commit()

## linking and sharing devices
# link devices
print("Linking Devices")
link = DeviceLink(user_id=maomao.id, device_id=device.id,mode="owner")
db.session.add(link)
db.session.commit()

#share device 1 to shield
link2 = DeviceLink(user_id=shield.id, device_id=device.id,mode="guest")
db.session.add(link2)
db.session.commit()

# make new device for shield
link3 = DeviceLink(user_id=shield.id, device_id=device2.id,mode="owner")
db.session.add(link3)
db.session.commit()

#share device 2 to maomao
link4 = DeviceLink(user_id=maomao.id, device_id=device2.id,mode="guest")
db.session.add(link4)
db.session.commit()

# share both devices to ohm
link5 = DeviceLink(user_id=ohm.id, device_id=device.id,mode="guest")
db.session.add(link5)
db.session.commit()
link6 = DeviceLink(user_id=ohm.id, device_id=device2.id,mode="guest")
db.session.add(link6)
db.session.commit()

## add locations to the db
print("Populating Locations")
# get the device with id 1
device = Device.query.filter_by(id=1).first()
# make location list
loc_json = ["13.726607559695099,100.50900220870973","13.724731518375952,100.50915241241456",
            "13.723439125628536,100.50902366638185","13.721552636338338,100.50889492034912",
            "13.720155999137464,100.5087447166443","13.718811467412552,100.50810098648073",
            "13.717237625918775,100.50732851028444","13.716091112226623,100.50624489784242"]
# manually add locations to the db
for i in loc_json:
    loc = Location(device_id=device.id, location=i, timestamp=datetime.now())
    db.session.add(loc)
    db.session.commit()

# get the device with id 2
device = Device.query.filter_by(id=2).first()
# make location list
loc_json = ["13.72723290346725,100.50898075103761", "13.728681610134073,100.50884127616884",
            "13.73014073010539,100.5084550380707", "13.730578464326411,100.5073392391205",
            "13.730953664436944,100.50615906715393","13.731297597344199,100.50502181053163"]
# manually add locations to the db
for i in loc_json:
    loc = Location(device_id=device.id, location=i, timestamp=datetime.now())
    db.session.add(loc)
    db.session.commit()

# print("MaoMao devices:", maomao.devices)
# print("Shield Devices:", shield.devices)
# print("Shield shared device:", DeviceLink.query.join(User).filter(User.id == shield.id).filter(DeviceLink.mode == "guest").first().device_id)
# print("Location Query:", Location.query.filter(Location.device_id == DeviceLink.query.join(User)\
#                                                .filter(User.id == shield.id)\
#                                                .filter(DeviceLink.mode == "guest").first().device_id).all()[0].timestamp)

# maomao = User.query.filter_by(username='maomao').first()
# device = Device.query.filter_by(id=2).first()
# ids = DeviceLink.query.join(User).filter(User.id == maomao.id).filter(DeviceLink.mode == "owner").all()
# for i in ids:
#     print("Device name from User ID", Device.query.filter_by(id=i.device_id).first())
# print("User ID from device:", DeviceLink.query.filter_by(device_id=device.id).filter_by(mode="owner").first().user_id)