import os


class Config:

    MAX_LENGTH = 128
    SECRET_KEY = os.environ.get("SECRET_KEY")
