from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_login import LoginManager
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object('app.config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
login_manager = LoginManager(app)
jwt = JWTManager(app)

blacklist = set()

@login_manager.user_loader
def load_user(user_id):
    from app.models import User
    return User.query.get(int(user_id))

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    return jti in blacklist

from app.models import *  # Import models
from app.routes import *  # Import routes
