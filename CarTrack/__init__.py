# flask imports
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from CarTrack.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from CarTrack.main.routes import main
    from CarTrack.users.routes import users
    from CarTrack.devices.routes import devices
    from CarTrack.errors.handlers import errors
    from CarTrack.location.routes import location

    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(devices)
    app.register_blueprint(errors)
    app.register_blueprint(location)

    return app