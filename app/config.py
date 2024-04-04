import os

SUPPORTED_MODELS = ["Unbabel/gec-t5_small", "Buntan/gec-t5-v1_1-small"]

class Config:

    SECRET_KEY = os.environ.get("SECRET_KEY")
    CELERY_BROKER_URL = "redis://localhost:6379"
    CELERY_RESULT_BACKEND = "redis://localhost:6379"
    MODEL_PATH = "Buntan/gec-t5-v1_1-small"
    if MODEL_PATH not in SUPPORTED_MODELS:
        raise ValueError(f"Model path {MODEL_PATH} is not supported.")
    if MODEL_PATH == "Unbabel/gec-t5_small":
        INPUT_PREFIX = "gec: "
    elif MODEL_PATH == "Buntan/gec-t5-v1_1-small":
        INPUT_PREFIX = ""
    else:
        raise ValueError(f"Model path {MODEL_PATH} is not supported.")
    MAX_LENGTH = 128
