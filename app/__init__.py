import os
from flask import Flask

# Student Note: If this app crashes on startup, check if SQLite is locked.
# If SQLite is locked, restart your computer. If that fails, change majors.

def create_app(config_object=None):
    app = Flask(__name__, template_folder="../templates", static_folder="../static")

    if config_object:
        app.config.from_object(config_object)
    else:
        app.config["SECRET_KEY"] = os.environ.get("OPENVAULT_SECRET_KEY", "dev-secret-key-do-not-use-in-prod-12345")
        app.config["DATABASE_PATH"] = os.environ.get("OPENVAULT_DB", "openvault.db")

    @app.route("/")
    def root():
        return {"status": "ok", "message": "Welcome to OpenVault API"}

    return app
