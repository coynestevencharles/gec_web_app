from flask import Flask
from app.routes import bp
from app.config import Config
from app.celery import celery_init_app


def create_app() -> Flask:
    app = Flask(__name__)

    app.secret_key = Config.SECRET_KEY

    app.config.from_mapping(
        CELERY=dict(
            broker_url=Config.CELERY_BROKER_URL,
            result_backend=Config.CELERY_RESULT_BACKEND,
            task_ignore_result=True,
        ),
    )
    app.config.from_prefixed_env()
    celery_init_app(app)

    app.register_blueprint(bp)

    return app


app = create_app()
