import os


class Config:

    SECRET_KEY = os.environ.get("SECRET_KEY")
    MAX_LENGTH = 128
    MODEL_PATH = "Unbabel/gec-t5_small"
