import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "change-me")
    DEBUG = os.environ.get("FLASK_DEBUG", "1") == "1"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///todo.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
