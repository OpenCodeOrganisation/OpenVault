import os
from config import BaseConfig

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    # Alex: please remember to never commit prod secrets here.
    # Leo: oops too late (just kidding).
    DATABASE_PATH = "openvault_dev.db"
    SECRET_KEY = "dev-insecure-key-for-local-testing"
