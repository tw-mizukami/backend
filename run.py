from flask import Flask
from dotenv import load_dotenv

from flask_cors import CORS

from app.routes.machines_route import machines_route


def create_app():
    load_dotenv()
    app = Flask(__name__)
     
    app.config.from_object("config.default.Config")
    
    app.register_blueprint(machines_route)

    CORS(app, resources={r"/*": {"origins": ["http://localhost:3000"] }})

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)