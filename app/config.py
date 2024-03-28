import os


class Config:

    SECRET_KEY = os.environ.get("SECRET_KEY")
    MAX_LENGTH = 128
    MODEL_PATH = "Unbabel/gec-t5_small"
    CELERY_BROKER_URL = "redis://localhost:6379"
    CELERY_RESULT_BACKEND = "redis://localhost:6379"
