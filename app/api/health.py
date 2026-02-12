"""
Application health check endpoint.
"""
from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)

@health_bp.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "app": "OpenVault",
        "version": "0.4.0",
        "vibes": "immaculate"
    }), 200
