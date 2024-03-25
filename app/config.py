import os


class Config:

    SECRET_KEY = os.environ.get("SECRET_KEY")
    MAX_LENGTH = 128
