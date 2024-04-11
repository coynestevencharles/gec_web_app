from flask import Flask
from celery import Celery, Task
from celery.signals import after_setup_logger
import logging.config
from app.logging_config import LOGGING_CONFIG


@after_setup_logger.connect
def setup_loggers(logger, *args, **kwargs):
    logging.config.dictConfig(LOGGING_CONFIG)


def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=FlaskTask)
    celery_app.config_from_object(app.config["CELERY"])
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app
