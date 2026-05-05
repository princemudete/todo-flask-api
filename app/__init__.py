from flask import Flask
from flask_cors import CORS

from .config import Config
from .models import db
from .routes import register_routes
from .schemas import ma


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        db.create_all()

    register_routes(app)
    return app
