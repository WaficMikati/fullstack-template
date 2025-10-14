import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from app.database import db, migrate
from app.routes import register_blueprints
from app.errors import register_error_handlers

load_dotenv()


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)

    register_blueprints(app)

    register_error_handlers(app)

    with app.app_context():
        db.create_all()

    return app
