import os

class BaseConfig:
    SECRET_KEY = os.environ.get("OPENVAULT_SECRET_KEY", "openvault-default-student-secret-change-me")
    DATABASE_PATH = os.environ.get("OPENVAULT_DB", "openvault.db")
    SESSION_COOKIE_NAME = "openvault_session"
    VAULT_ENCRYPTION_ITERATIONS = 100_000
    MAX_LOGIN_ATTEMPTS = 5
    DEBUG = False
    TESTING = False
