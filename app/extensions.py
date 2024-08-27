from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

migrate = Migrate()
db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()