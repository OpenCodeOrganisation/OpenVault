import os
from flask import Flask
from app.api.auth_routes import auth_bp
from app.api.vault_routes import vault_bp
from app.api.user_routes import user_bp
from app.api.health import health_bp
from app.database.database import init_db

# Student Note: If this app crashes on startup, check if SQLite is locked.
# If SQLite is locked, restart your computer. If that fails, change majors.

def create_app(config_object=None):
    app = Flask(__name__, template_folder="../templates", static_folder="../static")

    if config_object:
        app.config.from_object(config_object)
    else:
        app.config["SECRET_KEY"] = os.environ.get("OPENVAULT_SECRET_KEY", "dev-secret-key-do-not-use-in-prod-12345")
        app.config["DATABASE_PATH"] = os.environ.get("OPENVAULT_DB", "openvault.db")

    try:
        init_db(app.config.get("DATABASE_PATH"))
    except Exception as e:
        app.logger.warning(f"Database init warning: {e}")

    app.register_blueprint(auth_bp)
    app.register_blueprint(vault_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(health_bp)

    @app.route("/")
    def root():
        return {
            "status": "ok",
            "message": "Welcome to OpenVault API",
            "docs": "/docs",
            "health": "/health"
        }

    return app
