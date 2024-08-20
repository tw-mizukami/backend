from flask import Flask
from dotenv import load_dotenv

from flask_cors import CORS

from app import models
from app.routes.machineInfo_route import machineInfo_route
from app.routes.auth_route import auth_router
from app.extensions import db, ma, migrate


def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.json.ensure_ascii = False
     
    app.config.from_object("config.default.Config")
    
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(machineInfo_route)
    app.register_blueprint(auth_router)

    CORS(app, resources={r"/*": {"origins": ["http://localhost:3000"] }})

    return app



