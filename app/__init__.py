from flask import Flask
from app.routes import bp
from app.config import Config


def create_app():
    app = Flask(__name__)

    app.secret_key = Config.SECRET_KEY

    app.register_blueprint(bp)

    return app
