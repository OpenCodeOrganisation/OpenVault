import os
from config import BaseConfig

class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get("OPENVAULT_SECRET_KEY")
    DATABASE_PATH = os.environ.get("OPENVAULT_DB", "/var/lib/openvault/openvault.db")

    if not SECRET_KEY:
        # We don't want to crash during import, but log a loud warning
        # Alex: In prod this MUST be set in environment variables!
        SECRET_KEY = "TEMP_PRODUCTION_FALLBACK_MUST_BE_REPLACED"
