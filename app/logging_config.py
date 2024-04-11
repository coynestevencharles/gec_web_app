import os

LOG_DIR = os.path.join(os.getcwd(), "logs")

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "detailed": {
            "format": "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"
        }
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(LOG_DIR, "gec_web_app.log"),
            "maxBytes": 10240,
            "backupCount": 10,
            "formatter": "detailed",
        }
    },
    "root": {"level": "INFO", "handlers": ["file"]},
}
